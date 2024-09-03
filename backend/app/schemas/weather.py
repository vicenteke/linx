from pydantic import BaseModel, Field


class WeatherSchema(BaseModel):
    city: str = Field(max_length=150, description='city name')
    forecast_date: str = Field(description='date for the weather forecast')
    temperature: float = Field(description='temperature in celsius')
    wind: float = Field(description='wind speed')
    cloudiness: str = Field(max_length=150, description='cloudiness description')
    pressure: int = Field(description='pressure in hpa')
    humidity: int = Field(description='humidity percentage')
    sunrise: int = Field(description='sunrise timestamp')
    sunset: int = Field(description='sunset timestamp')
    latitude: float = Field(description='latitude coordinates')
    longitude: float = Field(description='longitude coordinates')
