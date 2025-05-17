from typing import List

from pydantic import BaseModel


class EcgReturn(BaseModel):
    ecg: List[List[float]]
    markup: List[List[int]] | None = None


class Verdict(BaseModel):
    user_id: str

    # Parameter fields
    P: bool
    Q: bool
    R: bool
    S: bool
    T: bool
    P_interval: bool
    QRS: bool
    T_interval: bool

    # Record fields
    sample_id: int
    comments: str


class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str