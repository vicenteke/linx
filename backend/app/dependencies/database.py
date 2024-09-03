from sqlalchemy.orm.session import Session
from ..db.models.database import SessionLocal


def get_db() -> Session:
    """ Dependency to create a DB session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
