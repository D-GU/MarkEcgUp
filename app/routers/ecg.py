from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.dp_depends import get_db
from app.models.patient import Patient
from app.models.user import User
from app.routers.auth import get_current_user
from app.schemas import EcgReturn
from app.service.ecg import get_patient_by_id

router = APIRouter(prefix="/ecgs", tags=["ecgs"])

# Здесь должна быть один эндпоинт
# Тот, который будет выводить пользователя на страницу с ЭКГ
# Где у него будет отображаться ЭКГ и его комментарии и параметры, которые он
# откомментировал

# Логика программы
# При  запуске сайта загружается endpoint
# show_patient_ecg_page, который бы загружал страницу с последним просмотренным ЭКГ для пользователя
# Также этот эндпоинт откликался на колбэки по смене пациента.
# В будущем также отображал коррекции пользователя

# @router.get("/")
# async def show_patient_ecg_page(
#         db: Annotated[AsyncSession, Depends(get_db)],
#         user: User = Depends(get_current_user),
#         is_first_load: Depends(is_first_load),
# )

MAX_PATIENTS = 21430

async def last_checked_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user)
) -> int:
    """
    Функция-зависимость, которая загружает из базы данных последнего проверенного пользователем пациента
    :param db: database
    :param user: Функция-зависимость возвращающая пользователя, от которого пришел запрос
    :return: int - порядковый номер пациента
    """
    last_checked_patient = await db.scalar(select(Patient.last_checked).where(
        Patient.user_id == user.id
    ))

    return last_checked_patient


async def get_current_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user)
) -> int:
    current_patient = await db.scalar(select(Patient.current_patient).where(
        Patient.user_id == user.id
    ))

    return current_patient


async def get_next_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
) -> int:
    current_patient = await get_current_patient(db, user)

    if current_patient == MAX_PATIENTS:
        return 0

    return current_patient + 1


async def get_prev_patient(
        db: Annotated[AsyncSession, Depends(get_db)],
        user: User = Depends(get_current_user),
) -> int:
    current_patient = await get_current_patient(db, user)

    if current_patient == 0:
        return 0

    return current_patient - 1


@router.get("/{patient_id}")
async def load_ecg_page_by_user_id(
        user: User = Depends(get_current_user),
        patient_id: int = Path(ge=0, lt=21430)
) -> dict:
    """
    Function that returns <<patient_id>> patients 12-lead ECG
    :param user:
    :param db:
    :param current_user: Dependency that get's current user
    :param patient_id: identification number of
    :return: EcgReturn
    """

    return {"ecg": get_patient_by_id(patient_id)}
