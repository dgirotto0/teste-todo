from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.user import UserLogin, UserRegister
from resources.task import TaskList, Task

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'admin'
jwt = JWTManager(app)

# Rotas da aplicação
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Adicionar recursos da API
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<string:task_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
