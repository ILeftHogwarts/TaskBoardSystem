from main.db import db_session
from main.models import *


class TaskBoardController:

    @classmethod
    def _serialize_many(cls, query):
        ser_data = [{'id': obj.id, 'caption': obj.caption} for obj in query]
        return ser_data

    @classmethod
    def _serialize_one(cls, obj: TaskBoard):
        return {'id': obj.id, 'caption': obj.caption}

    def get_taskboadrs(self, **kwargs):
        query = TaskBoard.query.filter_by(**kwargs).all()
        return self._serialize_many(query)

    def _validate_data(self, data):
        validated_data = [{'caption': obj_data.get('caption')} for obj_data in data]
        if not validated_data:
            raise Exception('Validation exception')
        return validated_data

    def create_taskboards(self, data):
        data = self._validate_data(data)
        objs = [TaskBoard(caption=obj_data['caption']) for obj_data in data]
        db_session.add_all(objs)
        db_session.commit()
        return self._serialize_many(objs)


class TaskController:

    @classmethod
    def _serialize_one(cls, obj: Task):
        return {
            'id': obj.id,
            'caption': obj.caption,
            'description': obj.description,
            'is_finished': obj.is_finished,
            'taskboard_id': obj.task_board_id
        }

    @classmethod
    def _serialize_many(cls, query):
        ser_data = [
            {
                'id': obj.id,
                'caption': obj.caption,
                'description': obj.description,
                'is_finished': obj.is_finished,
                'taskboard_id': obj.task_board_id
            } for obj in query
        ]
        return ser_data

    def get_taskboard_tasks(self, taskboard_id):
        query = Task.query.filter_by(task_board_id=taskboard_id).all()
        return self._serialize_many(query)

    def create_task(self, caption: str, taskboard_id: int, description=None):
        obj = Task(caption=caption, task_board_id=taskboard_id, description=description)
        db_session.add(obj)
        db_session.commit()
        return self._serialize_one(obj)

    def delete_task(self, task_id: int):
        Task.query.filter_by(id=task_id).delete()
        db_session.commit()

    def update_task(self, task_id: int, **kwargs):
        update_dict = {}
        if kwargs.get('caption'):
            update_dict['caption'] = kwargs.get('caption')
        if kwargs.get('description'):
            update_dict['description'] = kwargs.get('description')
        if kwargs.get('taskboard_id'):
            update_dict['task_board_id'] = kwargs.get('taskboard_id')
        if update_dict:
            db_session.query(Task).filter(Task.id == task_id).update(update_dict)
            db_session.commit()
        obj = Task.query.get(task_id)
        data = self._serialize_one(obj)
        return data

    def finish_task(self, task_id):
        obj = Task.query.get(task_id)
        obj.is_finished = True
        db_session.commit()
        return self._serialize_one(obj)
