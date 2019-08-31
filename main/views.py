from flask import jsonify, Blueprint, request

from main.controllers import TaskBoardController, TaskController

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/hello-world', methods=('GET',))
def hello_world():
    return jsonify({'Hello': 'Wolrd'})


@bp.route('/taskboard', methods=('GET',))
def get_taskboard_list():
    tb_ctrl = TaskBoardController()
    return jsonify(tb_ctrl.get_taskboadrs())


@bp.route('/taskboard', methods=('POST',))
def create_taskboards():
    data = request.get_json()
    print(data)
    tb_ctrl = TaskBoardController()
    objs_data = tb_ctrl.create_taskboards(data)
    return jsonify(objs_data), 201


@bp.route('/tasks/<taskboard_id>', methods=('GET',))
def get_taskboard_tasks(taskboard_id):
    task_ctrl = TaskController()
    data = task_ctrl.get_taskboard_tasks(taskboard_id)
    return jsonify(data)


@bp.route('/tasks', methods=('POST',))
def create_task():
    data = request.get_json()
    caption = data.get('caption')
    taskboard_id = data.get('taskboard_id')
    description = data.get('description')
    if not caption or not taskboard_id:
        return jsonify({'error': 'ValidationError', 'msg': 'Caption and TaskBoard id is required'}), 400
    task_ctrl = TaskController()
    obj_data = task_ctrl.create_task(caption, taskboard_id, description=description)
    return jsonify(obj_data), 201


@bp.route('/tasks/<task_id>', methods=('DELETE',))
def delete_tasks(task_id):
    task_ctrl = TaskController()
    task_ctrl.delete_task(task_id)
    return jsonify({'status': 'Task was deleted'})


@bp.route('/tasks/<task_id>', methods=('PATCH',))
def update_tasks(task_id):
    data = request.get_json()
    task_ctrl = TaskController()
    data = task_ctrl.update_task(task_id, **data)
    return jsonify(data)


@bp.route('/finish-task/<task_id>', methods=('POST',))
def finish_tasks(task_id):
    task_ctrl = TaskController()
    obj_data = task_ctrl.finish_task(task_id)
    return jsonify(obj_data)
