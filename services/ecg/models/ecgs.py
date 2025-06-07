from typing import *

from beanie import Document


class ECG(Document):
    patient_id: int
    lead_id: int
    signal: List[float]
    P: List[Optional[int]]
    P_Interval: List[int]
    Q: List[int]
    QRS_Interval: List[int]
    R: List[int]
    S: List[int]
    T: List[int]
    T_Interval: List[int]

    class Settings:
        name = "patient"
