from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from ..backend.db import Base
from ..models import user

class Patient(Base):
    __tablename__ = "patient"

    # Id fields
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    # Parameter fields
    P = Column(Boolean, default=None)
    Q = Column(Boolean, default=None)
    R = Column(Boolean, default=None)
    S = Column(Boolean, default=None)
    T = Column(Boolean, default=None)
    P_interval = Column(Boolean, default=None)
    QRS = Column(Boolean, default=None)
    T_interval = Column(Boolean, default=None)

    # Record fields
    sample_id = Column(Integer)
    comments = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship field
    user = relationship("User", back_populates="patient")