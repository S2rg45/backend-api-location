
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field


class CeleryTask(BaseModel):
    task: str = Field(..., example="")