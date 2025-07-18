from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Importing CORS middleware
from services.github_service import get_user_data


app = FastAPI()

@app.get("/github/{username}")
async def github_user_info(username: str):
    data = await get_user_data(username)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data


# Let connection from React app or frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React port 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)