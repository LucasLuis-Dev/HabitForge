from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from .base import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    frequency = Column(String(20), default="daily")
    target_reps = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class HabitExecution(Base):
    __tablename__ = "habits_executions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    executed_at = Column(DateTime(timezone=True), server_default=func.now())
    completed = Column(Boolean, default=False)