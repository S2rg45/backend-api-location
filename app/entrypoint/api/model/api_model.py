
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int] = Field(None, example=1)
    name: str = Field(..., example="Product 1")
    price: float = Field(..., example=10.0)
    in_stock: bool = Field(..., example=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    created_at: Optional[str] = Field(None, example="2021-01-01T00:00:00")
    email: str = Field(..., example="email@gmail.com")


class UserCreate(BaseModel):
    username: str = Field(..., example="")
    email: str = Field(..., example="smoreno@gmail.com")
    password: str = Field(..., example="password")


class UserLogin(BaseModel):
    email: str = Field(..., example="")
    password: str = Field(..., example="password")


class UserUpdate(BaseModel):
    email: Optional[str] = Field(None, example="")
    password: Optional[str] = Field(None, example="password")


class UserResponse(BaseModel):
    user: User
    token: Token


class UserList(BaseModel):
    users: List[User]


class ProductList(BaseModel):
    products: List[Product]


class ProductDelete(BaseModel): 
    id: str = Field(..., example=1)


class ProductCreate(BaseModel):
    name: str = Field(..., example="Product 1")
    description: Optional[str]= Field(..., example="Description of product 1")
    price: float = Field(..., example=10.0)
    in_stock: bool = Field(..., example=True)


class ProductUpdate(BaseModel):
    id: str = Field(..., example=1)
    name: Optional[str] = Field(None, example="Product 1")
    description: Optional[str] = Field(None, example="Description of product 1")
    price: Optional[float] = Field(None, example=10.0)
    in_stock: Optional[bool] = Field(None, example=True)




