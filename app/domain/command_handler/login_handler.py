

from app.domain.commands.login_command import Login


class LoginHandler:
    def __init__(self, login: Login):
        self.login = login

    def execute(self) -> dict:
        return {
            "email": self.login.email,
            "password": self.login.password
        }