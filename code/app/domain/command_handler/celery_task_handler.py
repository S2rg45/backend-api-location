

from app.domain.commands.celery_task_command import CeleryTask
from app.domain.ports.celery_location_port import CeleryLocationPort
from app.adapters.log.logger import Log



class CeleryTaskHandler:
    def __init__(self, task: CeleryTask):
        self.task = task
        self.log = Log()
        self.celery_task = CeleryLocationPort()
        
    
    async def get_status_task(self):
        self.log.logger.info(f"Task: {self.task}")
        result =  self.celery_task.get_task_status(self.task)
        self.log.logger.info(f"Task status: {result}")
        return result