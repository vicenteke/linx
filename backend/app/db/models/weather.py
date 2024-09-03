from sqlalchemy import (
    SmallInteger,
    Column,
    DateTime,
    Float,
    TIMESTAMP,
    UniqueConstraint,
    VARCHAR
)

from .base_model import BaseModel


class Weather(BaseModel):
    """
    Stores weather historical data

    Attributes
    ----------
    city: varchar(150)
        city name;
    forecast_date: date
        date for the weather forecast;
    temperature: float
        temperature in celsius;
    wind: float
        wind speed;
    cloudiness: varchar(150)
        cloudiness description;
    pressure: small int
        pressure in hpa;
    humidity: small int
        humidity percentage;
    sunrise: timestamp
        sunrise timestamp;
    sunset: timestamp
        sunset timestamp;
    latitude: float
        latitude coordinates;
    longitude: float
        longitude coordinates;
    """
    __tablename__ = 'weather'

    city = Column(VARCHAR(150), nullable=False, comment='city name', index=True)
    forecast_date = Column(
        DateTime,
        nullable=False,
        comment='date for the weather forecast',
        index=True
    )
    temperature = Column(
        Float,
        nullable=False,
        comment='temperature in celsius'
    )
    wind = Column(Float, nullable=False, comment='wind speed')
    cloudiness = Column(
        VARCHAR(150),
        nullable=False,
        comment='cloudiness description'
    )
    pressure = Column(SmallInteger, nullable=False, comment='pressure in hpa')
    humidity = Column(
        SmallInteger,
        nullable=False,
        comment='humidity percentage'
    )
    sunrise = Column(TIMESTAMP, nullable=False, comment='sunrise timestamp')
    sunset = Column(TIMESTAMP, nullable=False, comment='sunset timestamp')
    latitude = Column(Float, nullable=False, comment='latitude coordinates')
    longitude = Column(Float, nullable=False, comment='longitude coordinates')

    __table_args__ = (
        UniqueConstraint('city', 'forecast_date', "rm_timestamp"),
    )
