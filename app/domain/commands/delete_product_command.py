from typing import Optional

from pydantic import BaseModel


class DeleteProduct(BaseModel):
    id: str

