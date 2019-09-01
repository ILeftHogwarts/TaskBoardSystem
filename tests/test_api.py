import pytest
import json

from main import create_app
from main.models import *
from main.controllers import *
from main.db import db_session


@pytest.fixture
def client():
    app = create_app()
    return app


@pytest.fixture(scope='function')
def set_data():
    tb_obj = TaskBoard(caption='Test')
    db_session.add(tb_obj)
    task_obj = Task(caption='TestTask', description='TestTask', task_board_id=tb_obj.id)
    db_session.add(task_obj)
    db_session.commit()
    yield True
    TaskBoard.query.delete()
    Task.query.delete()


def test_taskboard_get(client):
    tb_obj = TaskBoard(caption='Test')
    db_session.add(tb_obj)
    db_session.commit()

    mocked_data = [
        {
            'caption': tb_obj.caption,
            'id': tb_obj.id
        }
    ]

    resp = client.test_client().get('/api/taskboard')
    assert resp.status == '200 OK'
    assert resp.json == mocked_data
    TaskBoard.query.delete()


def test_taskboard_create(client):
    data = [
        {
            'caption': 'Test'
        },
        {
            'caption': 'Test2'
        }
    ]
    resp = client.test_client().post('/api/taskboard', json=data)

    print(resp.json)

    objs = TaskBoard.query.all()
    tb_ctrl = TaskBoardController()
    mocked_data = tb_ctrl._serialize_many(objs)
    print(mocked_data)
    assert resp.status == "201 CREATED"
    assert resp.json == mocked_data


def test_task_get(client):
    obj = TaskBoard(caption='Test')
    db_session.add(obj)
    db_session.commit()
    task_obj = Task(caption='TestTask', description='Test', task_board_id=obj.id)
    db_session.add(task_obj)
    db_session.commit()

    resp = client.test_client().get(f'/api/tasks/{obj.id}')

    task_ctrl = TaskController()
    mocked_data = task_ctrl._serialize_one(task_obj)
    mocked_data = [mocked_data]
    print(mocked_data)
    print(resp.json)

    assert resp.status == "200 OK"
    assert resp.json == mocked_data


def test_task_create(client):
    obj = TaskBoard(caption='Test')
    db_session.add(obj)
    db_session.commit()

    data = {
        'caption': 'TaskTest2',
        'description': 'TaskTest2',
        'taskboard_id': obj.id,
    }

    resp = client.test_client().post('/api/tasks', json=data)
    print(resp.json)

    assert resp.status == "201 CREATED"


def test_task_update(client):
    obj = Task.query.first()

    data = {
        'caption': 'TotallyNewCaption',
        'description': 'TotallyNewDescription'
    }
    resp = client.test_client().patch(f'/api/tasks/{obj.id}', json=data)
    assert resp.status == "200 OK"
    assert resp.json['caption'] == data['caption']
    assert resp.json['description'] == data['description']


def test_task_finish(client):
    obj = Task.query.first()

    resp = client.test_client().post(f'/api/finish-task/{obj.id}')
    assert resp.status == "200 OK"
    assert resp.json['is_finished']


def test_task_delete(client):
    obj = Task.query.first()

    resp = client.test_client().delete(f'/api/tasks/{obj.id}')
    assert resp.status == "200 OK"
    assert resp.json['status'] == 'Task was deleted'

