from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from main.db import Base


__all__ = [
    'TaskBoard',
    'Task'
]


class TaskBoard(Base):
    __tablename__ = 'taskboards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String)


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String, unique=True)
    description = Column(String, nullable=True)
    is_finished = Column(Boolean, default=False)

    task_board_id = Column(Integer, ForeignKey('taskboards.id'), nullable=False)
