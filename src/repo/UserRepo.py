from src.models.UserModel import (
    UserModel,
    UserSchema,
    usersSchema,
    userSchemaWithSecret,
)
from src.repo.BaseRepo import BaseRepo
from utils.hash import hash as hash_function


class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def add_user(self, user: dict) -> dict:
        user["password"] = hash_function(user["password"])
        result = self.add(model=UserModel, schema=UserSchema, data=user)
        return result

    def get_users(self):
        with self.BaseSession(self.db_connector) as Session:
            users = Session.query(UserModel).all()
            result = usersSchema.dump(users)
        return result

    def find_by_email(self, user_login: dict):
        with self.BaseSession(self.db_connector) as Session:
            result = (
                Session.query(UserModel)
                .filter(UserModel.email == user_login.get("email", None))
                .first()
            )
        if result is None:
            raise Exception("Deu ruim")
            # TODO : Implementar exceções

        return userSchemaWithSecret.dump(result)
