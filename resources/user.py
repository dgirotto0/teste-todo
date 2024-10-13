from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp
from models.user_model import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Usuário é obrigatório")
    parser.add_argument('password', type=str, required=True, help="Senha é obrigatória")
    parser.add_argument('apelido', type=str, required=True, help="Apelido é obrigatório")  # Novo campo

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'Usuário já existe'}, 400

        user = UserModel(data['username'], data['password'], data['apelido'])
        user.save_to_db()

        return {'message': 'Usuário criado com sucesso'}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Usuário é obrigatório")
    parser.add_argument('password', type=str, required=True, help="Senha é obrigatória")

    def post(self):
        data = UserLogin.parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        if user and safe_str_cmp(user['password'], data['password']):
            access_token = create_access_token(identity=data['username'])
            return {'access_token': access_token}, 200
        return {'message': 'Credenciais inválidas'}, 401
