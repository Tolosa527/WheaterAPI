from pydantic import BaseModel
from typing import List, Optional

class Location(BaseModel):
    city: str
    country : str

class WeatherResponse(BaseModel):
    local_name: str
    temperature: str
    wind: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geo_coordinates: str
    requested_time: str
    cloudiness: str
