from typing import Union
from fastapi import FastAPI
from routes.router import router

app = FastAPI()
app.include_router(router)

