

from app.adapters.internal.redis import RedisAdapter
from app.adapters.internal.mongo import MongoAdapter
from app.adapters.log.logger import Log
from app.settings import config
import uuid


class LocationRegistry():
    def __init__(self):
        self.log = Log()
        self.redis_name = RedisAdapter(host="redis", port=6379, db=2)
        self.redis_uuid = RedisAdapter(host="redis", port=6379, db=1)  
        self.log.logger.info(f"Connection to config: {config["local"]["connection"]}")                                  
        self.mongo_adapter = MongoAdapter(host=config["local"]["connection"], 
                                          db_name=config["local"]["db_name"], 
                                          collection_name=config["local"]["collection_locations"])


    #validate if the location exists
    async def get_location(self, data):
        self.log.logger.info(f"Get location - registry port: {data.get('name')}")    
        response = await self.redis_name.exists(data.get("name"))
        self.log.logger.info(f"Response get location: {response}")        
        return  response
    
        
    #create a new location
    async def create_new_location(self, data):
        self.log.logger.info(f"Create new location - registry port: {data.get('name')}")
        data["uuid"] = str(uuid.uuid4())
        await self.redis_name.set_data(data.get("name"), data)
        await self.redis_uuid.set_data(data.get("uuid"), data)
        self.mongo_adapter.insert_data_collection(data)
        self.log.logger.info(f"Location created: {data.get('uuid')}")
        return data["uuid"]
    
    #get all locations
    async def get_all_locations_name(self):
        all_locations = await self.redis_name.get_all_keys()
        return all_locations
    

    #get all locations
    async def get_all_locations_uuid(self):
        all_locations = await self.redis_uuid.get_all_keys()
        return all_locations
    