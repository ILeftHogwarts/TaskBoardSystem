import pytest

from main import create_app
from main.models import  *
from main.controllers import *


@pytest.fixture
def client():
    app = create_app()
    return app

#
# @pytest.fixture
# def setup_db(app):
#     """A database for the tests."""
#     _db.app = app
#     with app.app_context():
#         _db.create_all()
#
#     yield _db
#
#     # Explicitly close DB connection
#     _db.session.close()
#     _db.drop_all()


def test_taskboard_get(client):
    resp = client.test_client().get('/api/taskboard')
    print(resp.data)
    assert resp.status == 200
    tb_ctrl = TaskBoardController()
    assert resp.data == tb_ctrl.get_taskboadrs()


# def test_taskboard_create(set_up):
#     pass
#
#
# def test_task_get(set_up):
#     pass
#
#
# def test_task_create(set_up):
#     pass
#
#
# def test_task_update(set_up):
#     pass
#
#
# def test_task_finish(set_up):
#     pass
#
#
# def test_task_delete(set_up):
#     pass
