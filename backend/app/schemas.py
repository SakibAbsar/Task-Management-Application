
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str
    deadline: datetime

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True
