

from app.adapters.internal.redis import RedisAdapter
from app.adapters.internal.mongo import MongoAdapter
from app.adapters.log.logger import Log
from app.adapters.internal.celery_adapter import run_test_task, get_task_result

from app.domain.ports.location_port import LocationRegistry
from app.settings import config
import math


class CeleryLocationPort:
    def __init__(self) -> None:
        self.log = Log()
        self.location_registry = LocationRegistry()
        self.redis = RedisAdapter(host="redis", port=6379, db=2)
        self.mongo_adapter_location = MongoAdapter(host=config["local"]["connection"], 
                                          db_name=config["local"]["db_name"], 
                                          collection_name=config["local"]["collection_locations"])
        self.mongo_adapter_status = MongoAdapter(host=config["local"]["connection"], 
                                          db_name=config["local"]["db_name"], 
                                          collection_name=config["local"]["collection_status"])
        

    
    async def validate_location(self, locations):
        """
        validate if the location exists
        """
        list_locations = []
        self.log.logger.info(f"Location to validate: {locations['locations']}")
        for location in locations['locations']:
            existence_location = await self.location_registry.get_location(location)
            if existence_location:
                return True
            location["process"] = "True"
            list_locations.append(location)
        self.log.logger.info(f"Location validated: {list_locations}")
        return list_locations
    

    async def create_location_redis(self, locations):
        """
        create locations in redis
        """
        self.log.logger.info(f"Location to create in Redis: {locations}")
        for location in locations:
            await self.location_registry.create_new_location(location)
        return locations

    
    async def calculate_distances_for_locations(self, locations):
        """
        create tasks to calculate distances between all locations
        """
        self.log.logger.info(f"Locations to calculate distances: {locations}")
        task_ids = []
        all_locations = self.mongo_adapter_location.get_collection_data()
        self.log.logger.info(f"data locations: {all_locations}")

        
        for location in locations:
            for item_location in all_locations:
                self.log.logger.info(f"Location: {location} and Item location: {item_location}")
                if location["name"] != item_location["name"]:
                    p = {"x": location["latitude"], "y": location["longitude"]}
                    q = {"x": item_location["latitude"], "y": item_location["longitude"]}
                    self.log.logger.info(f"Location: {p} and Item location: {q}")
                    result =  run_test_task(p, q)
                    self.log.logger.info(f"Task created: {result}")
                    # Guardar el task_id en MongoDB para seguimiento
                    save_result_id = self.mongo_adapter_status.insert_data_collection({
                        "task_id": result,
                        "point_1": p,
                        "point_2": q,
                        "status": "PENDING"
                    })
                    self.log.logger.info(f"Task saved: {save_result_id}")
                    task_ids.append(result)
        
        return task_ids


    def get_task_status(self, task_ids):
        """
        get task status
        """
        for task_id in task_ids:
            self.log.logger.info(f"Task id: {task_id.task}")
            task = get_task_result(task_id.task)
            self.log.logger.info(f"Task status: {task.state}")
            if task.state == "PENDING":
                self.log.logger.info(f"Task pending: {task_id.task}")
                return  {"task_id": task_id.task, "status": "Pending"}
            elif task.state == "SUCCESS":
                self.log.logger.info(f"Task completed: {task.result}")
                result = {"task_id": task_id.task, "status": "Completed", "task": task.result}
                self.mongo_adapter_status.get_data_and_update({"task_id": task_id}, {"status": task.state, "task_result": task.result})
                return result
            elif task.state == "FAILURE":
                self.log.logger.info(f"Task failed: {task.result}")
                result ={"task_id": task_id.task, "status": "Failed", "error": str(task.result)}
                self.mongo_adapter_status.get_data_and_update({"task_id": task_id}, {"status": task.state, "task_result": task.result})
                return result
            else:
                self.log.logger.info(f"Task status: {task.state}")
                return {"task_id": task_id.task, "status": task.state}

