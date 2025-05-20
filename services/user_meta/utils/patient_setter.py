from typing import Annotated

from fastapi import Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .user_key import get_current_user
from ..backend.dp_depends import get_db
from ..models.user import User

MAX_PATIENTS = 21430


async def set_current_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
        updated_patient: int = Query(ge=0, lt=MAX_PATIENTS)
) -> dict:
    user = await db.scalar(
        select(User).where(
            User.id == user.get("user_id")
        )
    )

    user.current_patient = updated_patient

    await db.commit()

    return {"updated_patient": updated_patient}
