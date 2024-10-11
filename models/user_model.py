from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['todo_db']
users_collection = db['users']

class UserModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return users_collection.find_one({'username': username})

    def save_to_db(self):
        users_collection.insert_one({'username': self.username, 'password': self.password})
