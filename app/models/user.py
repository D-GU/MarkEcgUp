from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.backend.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)