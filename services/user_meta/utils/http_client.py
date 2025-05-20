from fastapi import status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from httpx import AsyncClient

from ..schemas import User

security = HTTPBearer()


class HTTPClient:
    def __init__(self, base_url: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
        self._token = credentials.credentials
        self._session = AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {self._token}"}
        )


class UserKeyHttpClient(HTTPClient):
    async def get_current_user(self):
        async with self._session.get("/get_current_user") as response:
            if response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication credentials"
                )
            result = await response.json()
            return User(**result)
