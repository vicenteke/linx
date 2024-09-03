from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from ..dependencies.database import get_db
from ..schemas.weather import WeatherSchema
from ..db.repositories.search import SearchRepository
from ..db.repositories.weather import WeatherRepository


router = APIRouter(prefix='/weather')


@router.get("/{city}", response_model=List[WeatherSchema])
def get_weather_forecast(city: str, db_session: Session = Depends(get_db)):
    res = WeatherRepository(db_session).get_forecast(city)

    actual_city = res[0]['city']
    SearchRepository(db_session).create(city=actual_city, search=city)
    db_session.commit()

    return res
