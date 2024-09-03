from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from ..dependencies.database import get_db
from ..schemas.search import SearchSchema
from ..schemas.weather import WeatherSchema
from ..db.repositories.search import SearchRepository, Search
from ..db.repositories.weather import WeatherRepository


router = APIRouter()


@router.get("/forecast/{city}", response_model=List[WeatherSchema])
def get_weather_forecast(city: str, db_session: Session = Depends(get_db)):
    res = WeatherRepository(db_session).get_forecast(city)

    actual_city = res[0]['city']
    SearchRepository(db_session).create(city=actual_city, search=city)
    db_session.commit()

    return res


@router.get("/history", response_model=List[SearchSchema])
def get_search_history(
    search: str = None,
    city: str = None,
    limit: int = None,
    db_session: Session = Depends(get_db)
):
    payload = {}
    if search:
        payload['search'] = search
    if city:
        payload['city'] = city

    query = SearchRepository(db_session).query(**payload)\
        .order_by(Search.created_on.desc())
    if limit:
        query = query.limit(limit)

    res = query.all()
    return res
