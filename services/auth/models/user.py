from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from ..backend.db import Base
from ..models import patient


class User(Base):
    __tablename__ = "user"

    # Id fields
    id = Column(Integer, primary_key=True, index=True)

    # Credentials fields
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)

    # Records fields
    last_checked_patient = Column(Integer, default=0)
    current_patient = Column(Integer, default=0)

    # Relationship field
    patient = relationship(
        "Patient",
        uselist=False,
        single_parent=True,
        back_populates="user"
    )
