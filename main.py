from fastapi import FastAPI, HTTPException
from services.github_service import get_user_data

app = FastAPI()

@app.get("/github/{username}")
async def github_user_info(username: str):
    data = await get_user_data(username)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data
