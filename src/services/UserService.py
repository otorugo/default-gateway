from utils.hash import verify
from utils.jwt import create_acess_token


class UserService:
    @staticmethod
    def check_password(user_input: dict, user_db: dict):
        input_password = user_input.get("password")
        db_password = user_db.get("password")
        return verify(input_password, db_password)

    @staticmethod
    def validate_user_credentials(user_input: dict, user_db: dict):
        flag = UserService.check_password(user_input, user_db)
        if not flag:
            raise Exception("Wrong")

        return create_acess_token({"email": user_db.get("email")})
