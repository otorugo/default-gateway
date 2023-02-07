from fastapi import FastAPI

from src.controller.UserController import router

app = FastAPI()

app.include_router(router)
