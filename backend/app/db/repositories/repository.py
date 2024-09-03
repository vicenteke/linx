from sqlalchemy.sql import false, func, null
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from copy import copy

from ..models.database import Base


class Repository:
    """Defines an interface to interact with the DB.
    For each new ORM model, one should create a children class and
    implement queries related to that model inside its repository. The main
    purpose is to make it easier to manage queries, specially when there
    are model changes.

    Also, it is recommended to use it within a context (i.e. using the
    'with' keyword, see example below) whenever possible, because it will
    properly either commit or rollback your transactions.

    For instance:

    repositories/user.py:

        from ..models.user import User

        class UserRepository(Repository):
            def __init__(self, db_session):
                super().__init__(db_session, User)

            def get_current_user(self, id):
                return self.db_session.query(User.name).filter(...)
        ...

    somewhereelse.py

        from .repositories.user import UserRepository

        ...

        with UserRepository(self.db_session) as repo:
            current_user = repo.get_current_user(id)
    """

    UPDATE_PREFIX = "old__"  # Used on update() and create_or_update()

    def __init__(self, db_session: Session, model: Base):
        self.db_session = db_session
        self.model = model

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        if not exc_type and not exc_val:
            self.commit()
        else:
            self.rollback()

    def rollback(self):
        self.db_session.rollback()

    def commit(self):
        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.rollback()
            raise IntegrityError(e)

    def query(self, base_query=None, include_deleted=False, **kwargs):
        """Main method to create a query with filters. It will filter each
        parameter passed to it to be equals. You can override this whenever
        necessary, so special cases can be handled. There should be lots of
        examples in other repositories (a.k.a. repos).

        base_query: instead of using the default query, a base query can
                    be provided;
        include_deleted: if set to false, will exclude soft-deleted
                         entries;
        """

        # Define the base query
        query = (
            base_query if base_query is not None
            else self.db_session.query(self.model)
        )

        # Filter for deleted values if appliable
        if not include_deleted:
            query = query.filter(self.model.deleted == false())

        # Create filters
        for key, value in kwargs.items():
            if value is None:
                query = query.filter(getattr(self.model, key) == null())
            else:
                query = query.filter(getattr(self.model, key) == value)

        return query

    def all(self, **kwargs):
        return self.query(**kwargs).all()

    def one(self, **kwargs):
        return self.query(**kwargs).one()

    def one_or_none(self, **kwargs):
        return self.query(**kwargs).one_or_none()

    def first(self, **kwargs):
        return self.query(**kwargs).first()

    def count(self, **kwargs):
        base_query = self.db_session.query(func.count(self.model.pk))
        return self.query(base_query=base_query, **kwargs).scalar()

    def delete(self, **kwargs):
        """Soft-deletes entries"""
        entries = self.all(**kwargs)
        for entry in entries:
            entry.deleted = True

        if len(entries) == 1:
            return entries[0]

        return entries or None

    def paginate(self, page=0, per_page=None, **kwargs):
        """Method used to create pagination, where 'page' is the current page
        index and 'per_page' is the number of items per page.
        """
        if per_page is None:
            return self.all(**kwargs)

        page = int(page or 0)
        per_page = int(per_page or 0)
        if page < 0:
            page = 0
        if per_page <= 0:
            per_page = 10
        return self.query(**kwargs).offset(page * per_page).limit(per_page)\
            .all()

    def hard_delete(self, **kwargs):
        """CAUTION: this method will exclude your data permanently from the DB.
        """
        self.query(**kwargs).delete()

    def create(self, **kwargs):
        """Creates a new entry"""
        obj = self.model(**kwargs)
        self.db_session.add(obj)
        return obj

    def update(self, **kwargs):
        """Updates an entry if it exists and returns it, otherwise
        returns None.

        It will filter each arg with the prefix UPDATE_PREFIX. For example,
        assuming that UPDATE_PREFIX = 'old__':

            with UserRepository(self.db_session) as repo:
                repo.update(old__name='Vicente', old__age=13, name='Erbs',
                            occupation='Developer')

            This snippet will:
                1) Find all users where User.name == 'Vicente' and
                   User.age == 13;
                2) Will update all those entries, so User.name = 'Erbs' and
                   User.occupation = 'Developer';
                3) Return the users. If no user is found on 1), returns
                   None.
        """

        filtered_kwargs, purged_kwargs = \
            self._get_filtered_and_purged_kwargs(**kwargs)

        entries = self.all(**filtered_kwargs)

        # Return None if no entry found
        if not entries:
            return None

        # Update entries
        for entry in entries:
            for key, value in purged_kwargs.items():
                setattr(entry, key, value)

        if len(entries) == 1:
            return entries[0]

        return entries

    def create_or_update(self, **kwargs):
        """Will try to update an existing value; if it does not exist, create
        a ew entry. Check update() to better understand how it identifies
        the value to be updated.
        """
        res = self.update(**kwargs)
        if res is None:
            _, purged_kwargs = self._get_filtered_and_purged_kwargs(**kwargs)
            res = self.create(**purged_kwargs)

        return res

    def _get_filtered_and_purged_kwargs(self, **kwargs):
        """Splits the kwargs in two groups:
        - filtered: the ones starting with UPDATE_PREFIX or the
                    'include_deleted' arg;
        - purged: kwargs not in 'filtered'.

        It is used for update() and create_or_update(). Check update() for
        more information.
        """

        filtered_kwargs = {}
        if "include_deleted" in kwargs:
            filtered_kwargs["include_deleted"] = kwargs.pop("include_deleted")

        kwargs_copy = copy(kwargs)
        for key in kwargs_copy.keys():
            if key.startswith(self.UPDATE_PREFIX):
                new_key = key[len(self.UPDATE_PREFIX):]  # remove prefix
                filtered_kwargs[new_key] = kwargs.pop(key)

        purged_kwargs = kwargs

        return filtered_kwargs, purged_kwargs

    def get_instance(self, ref, str_column="", **kwargs):
        """
        Returns an instance based on a ref. If instance is an integer, use pk
        as reference. If instance is str, use str_column. Otherwise returns
        None.
        """

        if isinstance(ref, int):
            return self.one_or_none(pk=ref, **kwargs)
        if isinstance(ref, str):
            kwargs[str_column] = ref
            return self.one_or_none(**kwargs)

        return ref
