from pydantic import BaseModel

class Task(BaseModel):
    name : str
    description : str | None

class STaskAdd(BaseModel):
    name : str
    description : str | None

class STask(STaskAdd) :
    id : int
