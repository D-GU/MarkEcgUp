from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from ..backend.dp_depends import get_db
from ..models.user import User
from ..schemas import CreateUser

SECRET_KEY = "d7cf7b96b36d91f32a5d89b7e2b8ebf06a2968d25727239ba529d28384710f0c"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["auth"])
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def create_token(
        username: str,
        user_id: int,
        expires_delta: timedelta
):
    encode = {
        "username": username,
        "user_id": user_id,
    }

    expires = datetime.now() + expires_delta
    encode.update({"exp": expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def authenticate_user(
        db: Annotated[AsyncSession, Depends(get_db)],
        username: str, password: str
):
    user = await db.scalar(select(User).where(User.username == username))

    if (
            not user or
            not bcrypt_context.verify(password, user.password)
    ):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials !",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return user


@router.get("/current_user")
async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)]
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        user_id: int = payload.get("user_id")
        expire = payload.get("exp")

        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user !"
            )

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied !"
            )

        return {
            "user_id": user_id,
            "username": username
        }

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired !"
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user !"
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
        db: Annotated[AsyncSession, Depends(get_db)],
        create_user: CreateUser
):
    await db.execute(
        insert(User).values(
            username=create_user.username,
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            password=bcrypt_context.hash(create_user.password),
        )
    )

    await db.commit()

    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "User was successfully created !"
    }


@router.post("/token")
async def login(
        db: Annotated[AsyncSession, Depends(get_db)],
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(db, form_data.username, form_data.password)

    token = await create_token(
        user.username,
        user.id,
        expires_delta=timedelta(minutes=20)
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# @router.get("/read_current_user")
# async def read_current_user(
#         user: User = Depends(get_current_user)
# ):
#     return {"User": user}
