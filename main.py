from fastapi import FastAPI
from app.routes.admin import router as admin_router

app = FastAPI()

app.include_router(admin_router)
