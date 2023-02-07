from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, Boolean

from connectors.sql import db_connector


class UserModel(db_connector.Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    deleted = fields.Boolean()


userSchema = UserSchema()
