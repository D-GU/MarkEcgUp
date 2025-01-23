from typing import List

from pydantic import BaseModel


class EcgReturn(BaseModel):
    ecg: List[List[float]]
    markup: List[List[int]] | None = None
