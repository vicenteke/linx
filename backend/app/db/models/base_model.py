from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Integer
)
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property

from time import time

from .database import Base


class BaseModel(Base):
    """ Base table model from which actual tables must derive, so they include
        default fields.
    """
    __abstract__ = True

    pk = Column(BigInteger, primary_key=True, index=True)
    created_on = Column(DateTime, nullable=False, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), onupdate=func.now())
    rm_timestamp = Column(Integer, server_default='0')

    @classmethod
    @property
    def __tablename__(cls):
        return cls.__tablename__.lower()

    @hybrid_property
    def deleted(self):
        return self.rm_timestamp != 0

    @deleted.setter
    def deleted(self, val):
        if val:
            self.rm_timestamp = time()
        else:
            self.rm_timestamp = 0

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
