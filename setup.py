from src.models.UserModel import db_connector,UserModel


db_connector.Base.metadata.create_all(db_connector.engine)

newUser = UserModel(name="Victor Hugo", email="victorsilva698@gmail.com")

session = db_connector.Session()
session.add(newUser)
session.commit()