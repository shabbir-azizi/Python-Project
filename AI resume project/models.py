from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # One user can have many reports
    reports = relationship(
        "Report",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_text = Column(Text, nullable=False)
    user_goal = Column(String(255), nullable=False)
    result = Column(Text, nullable=False)

    # Each report belongs to one user
    user = relationship(
        "User",
        back_populates="reports"
    )