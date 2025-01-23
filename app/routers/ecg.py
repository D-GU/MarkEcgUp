from fastapi import APIRouter, Path, Depends

from app.schemas import EcgReturn
from app.service.ecg import get_patient_by_id

router = APIRouter(prefix="/ecgs", tags=["ecgs"])


@router.get("/{patient_id}")
async def get_patient_ecg_by_id(patient_id: int = Path(ge=0, lt=21430)) -> EcgReturn:
    """
    Function that returns <<patient_id>> patients 12-lead ECG
    :param patient_id: int
    :return: EcgReturn
    """

    patient_ecg = EcgReturn
    patient_ecg.ecg = get_patient_by_id(patient_id)
    return patient_ecg

# Нужно реализовать зависимость от текущего пользователя
# @router.get("/{user_id}")
# async def get_last_checked_patient(Depends("get_current_user")) -> EcgReturn:
#     """
#     Function that returns current users last checked 12-lead ECG
#     :param patient_id: int
#     :return: EcgReturn
#     """
#     # orm to db to get last checked patient
#     ret_ecg = EcgReturn
#     ret_ecg.ecg = ...
#     return ret_ecg