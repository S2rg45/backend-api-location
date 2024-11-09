import asyncio
import json
import uuid
from redis.asyncio import Redis


class RedisAdapter:
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db   = db
        self.redis = Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)


    async def set_data(self, key, data, expire=None):
        value = json.dumps(data)  # Convertimos el diccionario a JSON
        await self.redis.set(key, value, ex=expire)


    async def get_data(self, key):
        value = await self.redis.get(key)
        if value:
            return json.loads(value)  # Convertimos el JSON de vuelta a diccionario
        return None
    

    async def delete_data(self, key):
        await self.redis.delete(key)


    async def exists(self, key):
        return await self.redis.exists(key) == 1


    async def get_all_keys(self, pattern="*"):
        return await self.redis.keys(pattern)
    

    async def generate_and_store_uuid(self, data, expire=None):
        unique_id = str(uuid.uuid4())
        await self.set_data(unique_id, data, expire=expire)
        return unique_id
    
