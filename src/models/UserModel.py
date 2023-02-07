from enum import Enum

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum

from connectors.sql import db_connector


class Roles(Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class UserModel(db_connector.Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    role = Column(SQLEnum(Roles), nullable=False, default=Roles.USER.value)
    deleted = Column(Boolean, default=False, nullable=False)
    current_token = Column(String(181))


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()


class UserSchemaWithSecret(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()


userSchema = UserSchema()
userSchemaWithSecret = UserSchemaWithSecret()
usersSchema = UserSchema(many=True)


class UserToken(Schema):
    id = fields.Int()
    email = fields.Str()


userToken = UserToken()
