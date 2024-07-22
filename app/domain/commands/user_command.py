
from typing import Optional

from pydantic import BaseModel



class UserAuthenticate(BaseModel):
    username: str
    email: str
    


