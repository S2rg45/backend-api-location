
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field



class CreateLocation(BaseModel):
    name: str = Field(..., example="")
    latitude: str = Field(..., example="")
    longitude: str = Field(..., example="")

class Location(BaseModel):
    locations: list[Dict[str, Any]] = Field(..., example=[{"name": "location1", "latitude": "1.1", "longitude": "1.1"}])


class Task(BaseModel):
    task: str = Field(..., example="")