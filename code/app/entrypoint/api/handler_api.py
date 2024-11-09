
from fastapi import Header, APIRouter, HTTPException, File, UploadFile, Depends
import json
import traceback

from fastapi.responses import JSONResponse

# from app.adapters.security.validate_token import OAuth2PasswordBearerWithCookie

# oauth_scheme = OAuth2PasswordBearerWithCookie()

# Importing models

from app.entrypoint.api.model.api_model import Location, CreateLocation, Task

from app.domain.command_handler.location_handler import LocationHandler
from app.domain.command_handler.celery_location_handler import CeleryLocationHandler
from app.domain.command_handler.celery_task_handler import CeleryTaskHandler
from app.adapters.log.logger import Log

log = Log()
router = APIRouter(prefix="/api")

############################################################################################################
# endpoint to get information locations
############################################################################################################
# endpoint to register a new locations

############################################################################################################
# get all inoformation locations

@router.post('/process-location/')
async def process_location(location: Location):
    log.logger.info(f"Location: {location}")
    """
    This function is used to get all locations
    :return: all locations
    """
    try:
        request = location.dict()
        log.logger.info(f"Location-dict: {request}")
        location_handler = CeleryLocationHandler(request)
        log.logger.info(f"Location-handler: {location_handler}")
        response = await location_handler.execute()
        return JSONResponse(content={"result": response}, status_code=200)
    except BaseException as e:
        error_trace = traceback.format_exc()
        log.logger.error(f"Error process location: {str(e)}")
        log.logger.error(f"Error trace: {error_trace}")
        raise HTTPException(status_code=400, detail=str(e)) from e


# endpoint to get all locations
@router.get('/locations_name/')
async def get_locations():
    """
    This function is used to get all locations
    :return: all locations
    """
    try:
        location_handler = LocationHandler()
        response = await location_handler.execute_name()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        log.logger.error(f"Error get locations: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e)) from e
    
############################################################################################################
# endpoint to get information uuid locations

@router.get('/status_task/')
async def get_status_task(task: Task):
    """
    This function is used to get all locations
    :return: all locations
    """
    try:
        location_handler = CeleryTaskHandler(task)
        response = await location_handler.get_status_task()
        return JSONResponse(content={"result": response}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


# endpoint to get the user information
# @router.get('/users/me')
# async def read_users_me(user: User = Depends(oauth_scheme.validate_token)):
#     """
#     This function is used to get the user information
#     :return: user information
#     """
#     try:
#         user_handler = UserHandler()
#         response = user_handler.execute()
#         return JSONResponse(content={"result": response}, status_code=200)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e)) from e


############################################################################################################
# endpoint to information products
############################################################################################################

# endpoint to get information products
# @router.get('/products/')
# async def get_products():
#     """
#     This function is used to get information products
#     :return: information products
#     """
#     try:
#         product_handler = ListProductsHandler()
#         response = product_handler.execute()
#         return JSONResponse(content={"result": response}, status_code=200)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e)) from e


############################################################################################################


