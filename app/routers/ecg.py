from fastapi import APIRouter, Path, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import Annotated

from app.backend.dp_depends import get_db
from app.schemas import EcgReturn
from app.service.ecg import get_patient_by_id

router = APIRouter(prefix="/ecgs", tags=["ecgs"])

# Здесь должна быть один эндпоинт
# Тот, который будет выводить пользователя на страницу с ЭКГ
# Где у него будет отображаться ЭКГ и его комментарии и параметры, которые он
# откомментировал




# @router.get("/{patient_id}")
# async def get_patient_ecg_by_id(patient_id: int = Path(ge=0, lt=21430)) -> EcgReturn:
#     """
#     Function that returns <<patient_id>> patients 12-lead ECG
#     :param patient_id: int
#     :return: EcgReturn
#     """
#
#     patient_ecg = EcgReturn
#     patient_ecg.ecg = get_patient_by_id(patient_id)
#     return patient_ecg
