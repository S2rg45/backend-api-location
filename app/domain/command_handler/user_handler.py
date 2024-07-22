

import uuid
from datetime import datetime, timezone

from app.domain.commands.user_command import UserAuthenticate

class UserHandler:
    def __init__(self, user: UserAuthenticate):
        self.user = user

    def execute(self) -> dict:
        return {
            "username": self.user.username,
            "email": self.user.email,
        }

