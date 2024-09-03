import os
import requests
from datetime import datetime, timedelta
from sqlalchemy.orm.session import Session

from .repository import Repository
from ..models.weather import Weather


class WeatherRepository(Repository):
    def __init__(self, db_session: Session):
        super().__init__(db_session, Weather)

    def _get_or_clear_existing_entries(self, city: str):
        """Check for existing entries on DB to avoid inconsistencies"""
        initial_date = datetime.now()
        final_date = initial_date + timedelta(days=4)

        entries = self.query(city=city)\
            .filter(self.model.forecast_date >= initial_date)\
            .order_by(self.model.forecast_date)\
            .all()

        if entries:
            if final_date - entries[-1].forecast_date < timedelta(days=1):
                return [{
                    **entry.json(),
                    'sunset': entry.sunset.timestamp(),
                    'sunrise': entry.sunrise.timestamp(),
                    'forecast_date': str(entry.forecast_date),
                } for entry in entries]

            for entry in entries:
                entry.deleted = True

    def _get_data_from_open_weather(self, city: str):
        """Fetch weather forecast data from Open Weather API (more info at
        https://openweathermap.org/forecast5).
        """
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&"\
            f"units=metric&appid={os.environ['WEATHER_API_KEY']}"

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch forecast fot '{city}'")

        data = response.json()
        city_name = data['city']['name']
        latitude = data['city']['coord']['lat']
        longitude = data['city']['coord']['lon']
        sunrise_as_int = data['city']['sunrise']
        sunset_as_int = data['city']['sunset']
        sunrise = datetime.fromtimestamp(sunrise_as_int)
        sunset = datetime.fromtimestamp(sunset_as_int)

        res = self._get_or_clear_existing_entries(city_name)
        if res:
            return res

        res = []
        last_date = None
        for entry in data['list']:
            current_date = entry['dt_txt']
            if (not last_date or last_date != current_date) and current_date.endswith('12:00:00'):
                payload = {
                    'city': city_name,
                    'sunrise': sunrise,
                    'sunset': sunset,
                    'latitude': latitude,
                    'longitude': longitude,
                    'temperature': entry['main']['temp'],
                    'pressure': entry['main']['pressure'],
                    'humidity': entry['main']['humidity'],
                    'cloudiness': entry['weather'][0]['description'],
                    'wind': entry['wind']['speed'],
                    'forecast_date': entry['dt_txt']
                }
                res.append({**payload, 'sunrise': sunrise_as_int, 'sunset': sunset_as_int})
                self.create(**payload)
                last_date = current_date

        self.db_session.commit()
        return res

    def get_forecast(self, city: str):
        """Return forecast data for the next five days. If data does not
        exist on DB, fetch from Open Weather API.
        """

        res = self._get_or_clear_existing_entries(city)
        if res:
            return res

        return self._get_data_from_open_weather(city)
