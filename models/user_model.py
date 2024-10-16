from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGODB_URI'))
db = client['todo_db']
users_collection = db['users']

class UserModel:
    def __init__(self, username, password, apelido):
        self.username = username
        self.password = password
        self.apelido = apelido

    @classmethod
    def find_by_username(cls, username):
        return users_collection.find_one({'username': username})

    def save_to_db(self):
        users_collection.insert_one({
            'username': self.username,
            'password': self.password,
            'apelido': self.apelido
        })

    @classmethod
    def get_user_by_username(cls, username):
        return users_collection.find_one({'username': username}, {'_id': 0, 'apelido': 1})
