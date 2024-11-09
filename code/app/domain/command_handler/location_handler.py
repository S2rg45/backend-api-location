

from app.domain.ports.location_port import LocationRegistry


class LocationHandler:
    def __init__(self):
        pass

    async def execute_name(self):
        response = await LocationRegistry().get_all_locations_name()
        return response
    
    async def execute_uuid(self):
        response = await LocationRegistry().get_all_locations_uuid()
        return response