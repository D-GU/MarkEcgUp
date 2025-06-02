from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from httpx import AsyncClient, HTTPError
from pydantic import ValidationError

from ..schemas import User

# Используем OAuth2 Password Bearer схему для получения токена
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="http://localhost:8000/auth/token"
)


async def get_current_user(
        token: str = Depends(oauth2_scheme)
) -> User:
    try:
        async with AsyncClient(timeout=5.0) as client:
            response = await client.get(
                "http://localhost:8000/auth/current_user",
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
