
from fastapi import Header, APIRouter, HTTPException, File, UploadFile, Depends
import json
from email_validator import validate_email

from fastapi.responses import JSONResponse

from app.adapters.security.validate_token import OAuth2PasswordBearerWithCookie

oauth_scheme = OAuth2PasswordBearerWithCookie()

# Importing models

from app.entrypoint.api.model.api_model import User,Product, Token, UserCreate, UserLogin, UserUpdate, UserResponse, UserList, ProductList, ProductCreate, ProductUpdate, ProductDelete

from app.domain.command_handler.register_handler import RegisterHandler
from app.domain.command_handler.login_handler import LoginHandler
from app.domain.command_handler.user_handler import UserHandler
from app.domain.command_handler.create_product_handler import CreateProductHandler
from app.domain.command_handler.update_product_handler import UpdateProductHandler
from app.domain.command_handler.delete_product_handler import DeleteProductHandler
from app.domain.command_handler.list_product_handler import ListProductsHandler



router = APIRouter(prefix="/api")

############################################################################################################
# endpoint to get information users
############################################################################################################
# endpoint to register a new user
@router.post('/register/')
async def register(user: UserCreate):
    """
    This function is used to register a new user
    :return: result of register user
    """
    try:
        validate_email(user.email)
        
        request = {
        "username": user.username,
        "email": user.email,
        "password": user.password
        }
        handler = RegisterHandler(request)
        response = handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


# endpoint to login a user
@router.post('/login/')
async def login():
    """
    This function is used to login a user
    :return: result of login user
    """
    return JSONResponse(content={"result": "User logged in"}, status_code=200)


# endpoint to get the user information
@router.get('/users/me')
async def read_users_me(user: User = Depends(oauth_scheme.validate_token)):
    """
    This function is used to get the user information
    :return: user information
    """
    try:
        user_handler = UserHandler()
        response = user_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


############################################################################################################
# endpoint to information products
############################################################################################################

# endpoint to get information products
@router.get('/products/')
async def get_products():
    """
    This function is used to get information products
    :return: information products
    """
    try:
        product_handler = ListProductsHandler()
        response = product_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


# endpoint to create new products
@router.post('/products/')
async def create_products(product: ProductCreate,
                          current_access = Depends(oauth_scheme.validate_token)):
    """
    This function is used to create new products
    :return: result of create products
    """
    try:
        request = {
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "in_stock": product.in_stock
        }
        print(request)
        product_handler = CreateProductHandler(request)
        response = product_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    

# endpoint to update products
@router.put('/products/')
async def update_products(update_product: ProductUpdate,
                          current_access = Depends(oauth_scheme.validate_token)):
    """
    This function is used to update products
    :return: result of update products
    """
    try:
        request = {
            "id": update_product.id,
            "name": update_product.name,
            "description": update_product.description,
            "price": update_product.price,
            "in_stock": update_product.in_stock
        }

        update_product_handler = UpdateProductHandler(request)
        response = update_product_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    

# endpoint to delete products
@router.delete('/products/')
async def delete_products(delete_product: ProductDelete,
                          current_access = Depends(oauth_scheme.validate_token)):
    """
    This function is used to delete products
    :return: result of delete products
    """
    try:
        request = {
            "id": delete_product.id
        }
        print(request)
        delete_product_handler = DeleteProductHandler(request)
        response = delete_product_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


############################################################################################################


