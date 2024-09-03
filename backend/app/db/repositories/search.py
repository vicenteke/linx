from datetime import datetime
from sqlalchemy.orm.session import Session

from .repository import Repository
from ..models.search import Search


class SearchRepository(Repository):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Search)
