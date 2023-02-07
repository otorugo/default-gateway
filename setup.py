from src.models.UserModel import UserModel, userSchema, db_connector
db_connector.Base.metadata.create_all(db_connector.engine)

