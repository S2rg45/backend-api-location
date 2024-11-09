
from app.domain.commands.celery_location_command import CeleryLocation
from app.domain.ports.celery_location_port import CeleryLocationPort
from app.adapters.log.logger import Log



class CeleryLocationHandler:
    def __init__(self, register_location: CeleryLocation):
        self.register_location = register_location
        self.log = Log()
        self.celery_location = CeleryLocationPort()

    async def execute(self):
        self.log.logger.info(f"Register location: {self.register_location}")
        validate_location = await self.celery_location.validate_location(self.register_location)
        if validate_location == True:
            self.log.logger.info(f"Location already exists: {self.register_location}")
            return {"message": "location already exists"}
        else:
            self.log.logger.info(f"Location to create: {validate_location}")
            await self.celery_location.create_location_redis(validate_location)
            data = await self.celery_location.calculate_distances_for_locations(validate_location)
            return data
        
    