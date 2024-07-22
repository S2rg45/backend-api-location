from typing import Optional

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    in_stock: bool