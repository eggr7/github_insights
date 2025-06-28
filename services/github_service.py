import httpx

BASE_URL = "https://api.github.com"

async def get_user_data(username: str):
    async with httpx.AsyncClient() as client:
        user_resp = await client.get(f"{BASE_URL}/users/{username}")
        if user_resp.status_code != 200:
            return None
        
        user_data = user_resp.json()

        followers_resp = await client.get(f"{BASE_URL}/users/{username}/followers")
        following_resp = await client.get(f"{BASE_URL}/users/{username}/following")

        followers = {f['login'] for f in followers_resp.json()}
        following = {f['login'] for f in following_resp.json()}

        not_following_back = following - followers

        return {
            "username": username,
            "name": user_data.get("name"),
            "bio": user_data.get("bio"),
            "public_repos": user_data.get("public_repos"),
            "followers_count": user_data.get("followers"),
            "following_count": user_data.get("following"),
            "followers": list(followers),
            "following": list(following),
            "not_following_back": list(not_following_back),
        }
