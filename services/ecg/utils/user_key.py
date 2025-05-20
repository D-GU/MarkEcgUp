from fastapi.security import HTTPBearer

from .http_client import UserKeyHttpClient

security = HTTPBearer()
client = UserKeyHttpClient(base_url="http://auth-service")


async def get_current_user():
    return await client.get_current_user()
