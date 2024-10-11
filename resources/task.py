import json
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task_model import TaskModel
from utils.cache import cache
from bson.objectid import ObjectId

class TaskList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help="O título não pode ser vazio.")

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()  # Obtém o ID do usuário do JWT
        tasks = cache.get(f'tasks_{user_id}')
        if tasks:
            tasks = json.loads(tasks)  # Desserializa o JSON para um objeto Python
        else:
            tasks = TaskModel.get_user_tasks(user_id)  # Obtém tarefas associadas ao usuário
            cache.set(f'tasks_{user_id}', json.dumps(tasks))  # Armazena as tarefas do usuário
        return {'tasks': tasks}, 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = TaskList.parser.parse_args()
        task_id = TaskModel.create_task(data['title'], user_id)  # Associa tarefa ao usuário
        cache.delete(f'tasks_{user_id}')
        return {'message': 'Tarefa criada', 'task_id': str(task_id)}, 201

class Task(Resource):
    @jwt_required()
    def put(self, task_id):
        user_id = get_jwt_identity()
        data = {'status': 'completa'}
        TaskModel.update_task(ObjectId(task_id), data, user_id)
        cache.delete(f'tasks_{user_id}')
        return {'message': 'Tarefa atualizada'}, 200

    @jwt_required()
    def delete(self, task_id):
        user_id = get_jwt_identity()
        TaskModel.delete_task(ObjectId(task_id), user_id)
        cache.delete(f'tasks_{user_id}')
        return {'message': 'Tarefa removida'}, 200
