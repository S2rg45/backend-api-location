

from app.domain.commands.register_command import Registers
from app.domain.ports.user_registry_port import UserRepository


class RegisterHandler:
    def __init__(self, register: Registers):
        self.register = register

    def execute(self):
        print(self.register)
        data = UserRepository().get_data_user(self.register)
        print(data)
        if data is not None:
            print("User already exists")
            return {"message": "User already exists"}
        else:
            print("User created")
            UserRepository().create_new_user(self.register)
            return {"message": "User created successfully"}


        