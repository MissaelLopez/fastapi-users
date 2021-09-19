from fastapi import FastAPI
from routes.api import api

app = FastAPI()

app.include_router(api)