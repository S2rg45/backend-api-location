
from typing import Optional, Any, Dict

from pydantic import BaseModel, Field


class CeleryLocation(BaseModel):
    locations: list[Dict[str, Any]] = Field(..., example=[{"name": "location1", "latitude": "1.1", "longitude": "1.1"}])
