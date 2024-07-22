from typing import Optional

from pydantic import BaseModel


class UpdateProduct(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    in_stock: Optional[bool]
