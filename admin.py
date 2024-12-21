from fastapi import APIRouter, HTTPException, Request
from app.utils import allowed_users
import json

router = APIRouter()


@router.get("/admin")
async def admin_access(request: Request):
    name = request.headers.get("name")
    password = request.headers.get("password")

    user = next((user for user in allowed_users if user["name"] == name and user["password"] == password), None)

    if user is None:
        raise HTTPException(status_code=403, detail="Access denied")

    return {"message": "Access granted", "user": name}
