from src.repo.BaseRepo import BaseRepo

# db_connector.Base.metadata.create_all(db_connector.engine)
# print(type(db_connector.Base))
# Insert snippet
# with BaseSession(db_connector) as Session:
#     new_user = UserModel(name="torugo", email="my_email", password="123123")
#     Session.add(newUser)
#     Session.commit()

base_repo = BaseRepo()

user = {
    "name": "Victor Hugo",
    "email": "victorsi@gmail.com",
    "password": "123123",
}

# User repo add implementation
# def add_user(user: dict):
#     user["password"] = hash(user["password"])
#     result = base_repo.add(model=UserModel, schema=UserSchema, data=user)
#     print(result)
#
#
# add_user(user)
