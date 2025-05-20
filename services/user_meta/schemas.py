from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str


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