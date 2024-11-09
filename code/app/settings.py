import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de entorno
config = {
  "local": {
    "connection": os.getenv("URI_DB_MONGO_LOCAL"),
    "collection_locations": os.getenv("COLLECTIONS_LOCATIONS"),
    "collection_status": os.getenv("COLLECTIONS_STATUS"),
    "db_name": os.getenv("DB_NAME"),
    "algorithm": os.getenv("ALGORITHM"),
    "jwt_secret_key": os.getenv("JWT_SECRET_KEY"),
    "jwt_refresh_secret_key": os.getenv("JWT_REFRESH_SECRET_KEY"),
    "access_token_expire_minutes": os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"),
    "refresh_token_expire_minutes": os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"),
  },
  "development": {
    "connection": os.getenv("URI_DB_MONGO_DEV")
  },
  "test": {
    "connection" : os.getenv("URI_DB_MONGO_TEST")
  }
}