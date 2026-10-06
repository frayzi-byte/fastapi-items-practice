from fastapi import APIRouter
from schemas import STaskAdd
from repository import TaskRepository

router = APIRouter(prefix='/items')

@router.post('/')
async def post_tasks(new_task : STaskAdd):
    task_id = await TaskRepository.add_one(new_task)
    return {"OK" : True, "TASK_ID" : task_id}

@router.get('/')
async def get_all_tasks():
    tasks = await TaskRepository.get_all()
    return {"data" : tasks}