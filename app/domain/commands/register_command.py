from typing import Optional

from pydantic import BaseModel, Field


class Registers(BaseModel):
    username: str = Field(..., example="")
    email: str = Field(..., example="")
    password: str = Field(..., example="password")
