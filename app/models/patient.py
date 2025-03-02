from sqlalchemy import ForeignKey, Column, Integer, String

from app.backend.db import Base


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    parameter = Column(String)
    x_coord = Column(Integer)
    comments_to_parameter = Column(String)
    verdict = Column(Integer)
    last_checked_patient = Column(Integer, default=0)
    current_patient = Column(Integer, default=0)
    # user = relationship("User", uselist=False, back_populates="patient")
