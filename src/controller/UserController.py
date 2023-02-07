from fastapi import APIRouter

from src.dto.user.UserDTO import UserInputDTO, UserOutputDTO, UserLoginInputDTO
from src.repo.UserRepo import UserRepo
from src.services.UserService import UserService

router = APIRouter(prefix="/user")


@router.post("/signup")
def new_user(user: UserInputDTO):
    try:
        user_repo = UserRepo()
        result = user_repo.add_user(user.dict())
        return UserOutputDTO(**result)
    except Exception as e:
        raise e


@router.post("/login")
def login(user_login: UserLoginInputDTO):
    try:
        user_repo = UserRepo()
        result = user_repo.find_by_email(user_login.dict())
        token = UserService.validate_user_credentials(
            user_login.dict(), result
        )
        return {"token": token}
    except Exception as e:
        raise e


# TODO : APAGAR ESSE ENDPOINT
@router.get("/")
def get_users():
    try:
        user_repo = UserRepo()
        result = user_repo.get_users()
        return {"result": result}
    except Exception as e:
        raise e
