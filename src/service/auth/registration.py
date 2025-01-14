from dataclasses import dataclass

from config.database import get_db
from core.service import BaseService
from models.user import UserBase



@dataclass
class RegisterUser(BaseService):
    """Create and Registr user in the sysytem"""
    username: str
    password: str
    first_name: str
    last_name: str

    def execute(self):
        print(self.create_user())

    def get_password_hash(self):
        pass

    def create_user(self):
        with get_db() as db:
            user = UserBase(
                username=self.username, 
                first_name=self.first_name,
                last_name=self.last_name,
            )
            user.set_password(self.password)
            db.add(user)
            db.commit()
            db.refresh(user)
        return user

    def validate(self):
        """Checking that a user with the same username does not exist"""

        return super().validate()