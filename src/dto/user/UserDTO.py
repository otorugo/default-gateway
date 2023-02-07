from pydantic import BaseModel


class UserInputDTO(BaseModel):
    name: str
    email: str
    password: str


class UserOutputDTO(BaseModel):
    name: str


class UserLoginInputDTO(BaseModel):
    email: str
    password: str


class UserLoginOutputDTO(BaseModel):
    email: str
    password: str
