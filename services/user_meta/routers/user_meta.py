from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException, status, Body
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..backend.dp_depends import get_db
from ..models.patient import Patient
from ..models.user import User
from ..schemas import Verdict
from ..utils.patient_setter import set_current_patient
from ..utils.user_key import get_current_user

router = APIRouter(prefix="/user_meta", tags=["user_meta"])
MAX_PATIENTS = 21429


@router.get("/patients")
async def get_last_checked_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user)
):
    try:
        last_checked_patient = await db.scalar(select(User.last_checked_patient).where(
            User.id == user.get("user_id")
        ))
    except AttributeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No records found !"
        )

    await set_current_patient(db, user, last_checked_patient)

    return {
        "User": user,
        "last_checked_patient": last_checked_patient
    }


@router.get("/patients")
async def get_current_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user)
) -> dict:
    current_patient = await db.scalar(select(User.current_patient).where(
        User.id == user.get("user_id")
    ))

    return {"current_patient": current_patient}


@router.post("/verdicts")
async def post_verdict(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
        verdict: Verdict = Body()
) -> dict:
    user_id = user.get("user_id")

    await db.execute(
        insert(Patient).values(
            user_id=user_id,
            P=verdict.P,
            Q=verdict.Q,
            R=verdict.R,
            S=verdict.S,
            T=verdict.T,
            P_interval=verdict.P_interval,
            QRS=verdict.QRS,
            T_interval=verdict.T_interval,
            sample_id=verdict.sample_id,
            comments=verdict.comments
        )
    )

    await db.commit()

    return {"message": "Вердикт был успешно отправлен !"}


@router.delete("/verdicts")
async def delete_verdict(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
        verdict_id: int = Query()
) -> dict:
    user_id = user.get("user_id")

    await db.execute(
        delete(Patient).where(
            Patient.user_id == user_id,
            Patient.id == verdict_id
        )
    )

    await db.commit()

    return {"message": "Verdict deleted !"}


@router.get("/verdicts")
async def get_verdicts(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
        sample_id: int = Query(ge=0, le=MAX_PATIENTS)
):
    user_id = user.get("user_id")

    verdicts = await db.scalars(
        select(Patient).where(
            Patient.sample_id == sample_id
        )
    )

    return verdicts.all()


@router.get("/verdicts/sample_id")
async def get_user_verdict(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
        sample_id: int = Query(ge=0, le=MAX_PATIENTS)
):
    user_id = user.get("user_id")

    verdict = await db.scalar(
        select(Patient).where(
            Patient.user_id == user_id and
            Patient.sample_id == sample_id
        )
    )

    if not verdict:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return verdict
