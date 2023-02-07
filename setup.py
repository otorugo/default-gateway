from src.models.UserModel import db_connector

db_connector.Base.metadata.create_all(db_connector.engine)

# Insert snippet
# with BaseSession(db_connector) as Session:
#     newUser = UserModel(name="torugo", email="my_email", password="123123")
#     Session.add(newUser)
#     Session.commit()
