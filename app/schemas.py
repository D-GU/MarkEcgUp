from typing import List

from pydantic import BaseModel


class EcgReturn(BaseModel):
    ecg: List[List[float]]
    markup: List[List[int]] | None = None

class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str