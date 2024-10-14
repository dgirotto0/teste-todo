# To-Do App - Flask & MongoDB

Este é um projeto de uma aplicação de gerenciamento de tarefas (To-Do List) desenvolvida em Python com Flask para o back-end, MongoDB para o banco de dados, e uma interface simples com HTML, CSS e JavaScript no front-end. O projeto foi implantado no Heroku e está disponível publicamente.

### Link da aplicação: [To-Do List](https://todo-python-teste-3f37d2b66a72.herokuapp.com/)

## Funcionalidades
A aplicação permite aos usuários:
- **Registrar e autenticar**: Usuários podem se registrar com um apelido e autenticar via JWT.
- **Adicionar novas tarefas**: Cada usuário pode adicionar suas próprias tarefas.
- **Listar tarefas**: Exibe uma lista de todas as tarefas de um usuário.
- **Marcar tarefas como completas**: Os usuários podem marcar tarefas como concluídas.
- **Remover tarefas**: Permite a exclusão de tarefas.
- **Compartilhar**: Opção para compartilhar a aplicação via WhatsApp ou outras plataformas.

## Tecnologias Utilizadas

### Back-end:
- **Python 3.12**: Linguagem principal do projeto.
- **Flask**: Framework para criar a API RESTful.
- **MongoDB Atlas**: Banco de dados não relacional para persistência das tarefas e cache (substituindo o Redis).
- **JWT (JSON Web Tokens)**: Para autenticação dos usuários e segurança.

### Front-end:
- **HTML/CSS**: Interface simples e responsiva para o usuário.
- **JavaScript**: Para manipulação dinâmica do DOM e comunicação com a API usando AJAX.

### Deploy e Infraestrutura:
- **Heroku**: Plataforma de nuvem usada para hospedar a aplicação.
- **MongoDB Atlas**: Gerenciamento dos dados na nuvem com alta disponibilidade.

## Instalação e Execução Local

### Pré-requisitos
- **Python 3.12+**
- **MongoDB Atlas**: Um cluster no MongoDB Atlas ou uma instância local.
- **Heroku CLI** (se quiser implantar em Heroku).

1. Clone o repositório:
   ```bash
   git clone https://github.com/dgirotto0/teste-todo.git
   cd teste-todo
   ```
2. Crie um ambiente virtual
   - **Para Linux/MacOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   - **Para Windows**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure a variável de ambiente MONGODB_URI com a URI do MongoDB Atlas:
   ```bash
   export MONGODB_URI="sua-uri-mongodb"
   ```
6. Execute o aplicativo:
   ```bash
   python app.py
   ```

## Deploy no Heroku
1. Certifique-se de que o Heroku CLI está instalado:
    ```bash
    heroku --version
    ```
3. Faça login no Heroku:    
    ```bash
    heroku login
    ```
5. Crie uma aplicação no Heroku:    
    ```bash
    heroku create todo-python-teste
    ```   
6. Adicione o MongoDB Atlas como variável de ambiente:    
    ```bash
    heroku config:set MONGODB_URI="sua-uri-mongodb"
    ```
7. Faça o deploy para o Heroku:    
    ```bash
    git push heroku main
    ```
6. Acesse a aplicação no link fornecido pelo Heroku.
    
