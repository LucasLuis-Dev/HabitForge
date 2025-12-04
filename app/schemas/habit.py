from pydantic import BaseModel
from datetime import datetime

class HabitBase(BaseModel):
    name: str
    frequency: str = "daily"
    target_reps: int = 1

class HabitCreate(HabitBase):
    pass

class HabitOut(HabitBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True