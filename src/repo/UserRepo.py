from src.models.UserModel import UserModel, UserSchema
from src.repo.BaseRepo import BaseRepo


class UserRepo(BaseRepo):

    def __init__(self):
        super.__init__()

    def add_user(self, user: dict) -> dict:
        user["password"] = hash(user["password"])
        result = self.add(model=UserModel, schema=UserSchema, data=user)
        return result
