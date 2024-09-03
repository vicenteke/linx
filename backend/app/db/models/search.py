from sqlalchemy import (
    Column,
    UniqueConstraint,
    VARCHAR
)

from .base_model import BaseModel


class Search(BaseModel):
    """
    Stores search history

    Attributes
    ----------
    search: varchar(150)
        search query;
    city: varchar(150)
        computed city name;
    """
    __tablename__ = 'searches'

    search = Column(VARCHAR(150), nullable=False, comment='search query')
    city = Column(VARCHAR(150), nullable=False, comment='actual city name', index=True)

    __table_args__ = (
        UniqueConstraint('created_on', "rm_timestamp"),
    )
