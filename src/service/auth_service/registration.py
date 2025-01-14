from dataclasses import dataclass

from core.service import BaseService



@dataclass
class RegisterUser(BaseService):
    """Create and Registr user in the sysytem"""
    username: str
    password: str
    first_name: str
    last_name: str

    def execute(self):
        pass

    def get_password_hash(self):
        pass

    def create_user(self):
        pass

    def validate(self):
        """Checking that a user with the same username does not exist"""

        return super().validate()