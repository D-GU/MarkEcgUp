from typing import List

from fastapi import APIRouter, Query, Depends, HTTPException, status

from ..models.ecg import ECG
from ..models.user import User
from ..utils.user_key import get_current_user

router = APIRouter(prefix="/ecg", tags=["ecg"])
MAX_PATIENTS = 21430  # Сделать это переменной окружения


@router.get("/ecgs", response_model=List[ECG])
async def get_patient_ecg_and_parameters(
        # user: User = Depends(get_current_user),
        sample_id: int = Query(ge=0, lt=MAX_PATIENTS)
):
    patient = await ECG.find({"patient_id": sample_id}).to_list()

    if not patient:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return patient
