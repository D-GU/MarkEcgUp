from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.backend.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    last_seen = Column(DateTime)
    last_checked_patient = Column(Integer, ForeignKey("patients.id"))
    relationship("Patient", uselist=False, single_parent=True, back_populates="user")



