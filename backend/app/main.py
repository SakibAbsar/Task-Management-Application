
from fastapi import FastAPI, Depends
from .models import Base, Task
from .schemas import TaskCreate, TaskRead
from .crud import create_task, get_tasks
from .dependencies import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/tasks/", response_model=TaskRead)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@app.get("/tasks/", response_model=list[TaskRead])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db=db, skip=skip, limit=limit)
