from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['todo_db']
tasks_collection = db['tasks']

class TaskModel:
    @staticmethod
    def create_task(title, user_id):
        task = {'title': title, 'status': 'pendente', 'user_id': user_id}
        result = tasks_collection.insert_one(task)
        return result.inserted_id

    @staticmethod
    def get_user_tasks(user_id):
        tasks = list(tasks_collection.find({'user_id': user_id}))
        for task in tasks:
            task['_id'] = str(task['_id'])
        return tasks

    @staticmethod
    def update_task(task_id, data, user_id):
        tasks_collection.update_one({'_id': task_id, 'user_id': user_id}, {'$set': data})

    @staticmethod
    def delete_task(task_id, user_id):
        tasks_collection.delete_one({'_id': task_id, 'user_id': user_id})
