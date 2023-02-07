from src.models.UserModel import UserModel, userSchema, db_connector
# db_connector.Base.metadata.create_all(db_connector.engine)
#
newUser = UserModel(name="Victor Hugo", email="victors@gmail.com")
#
# session = db_connector.Session()
# session.add(newUser)
# session.commit()
#
#
print(userSchema.dump(newUser))
#
