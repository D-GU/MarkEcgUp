from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    parameter = Column(String)
    x_coord = Column(Integer)
    comments_to_parameter = Column(String)
    verdict = Column(Integer)
    user = relationship("User", back_populates="patient")
