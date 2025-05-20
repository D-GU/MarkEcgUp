from typing import Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from httpx import AsyncClient, HTTPError
from pydantic import ValidationError

from ..schemas import User

# Используем OAuth2 Password Bearer схему для получения токена
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://auth-service/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    Dependency to retrieve and validate the current user from the auth-service using OAuth2 token.
    Raises:
      - 401 при некорректном или просроченном токене.
      - 503 если auth-service недоступен.
      - 502 если полученные данные невалидны.
    """
    try:
        async with AsyncClient(timeout=5.0) as client:
            response = await client.get(
                "http://auth-service/get_current_user",
                headers={"Authorization": f"Bearer {token}"}
            )
            response.raise_for_status()
    except HTTPError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Auth service unavailable"
        )

    payload: Any = response.json()
    try:
        return User(**payload)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Invalid data received from auth service"
        )
