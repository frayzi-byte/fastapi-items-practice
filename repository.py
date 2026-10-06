from database import new_session, TaskOrm
from schemas import STaskAdd
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, task : STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()

            new_task = TaskOrm(**task_dict)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models