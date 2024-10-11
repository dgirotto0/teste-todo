let accessToken = '';

document.getElementById('register-btn').addEventListener('click', () => {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;

    fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
    });
});

document.getElementById('login-btn').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.access_token) {
            accessToken = data.access_token;
            document.getElementById('auth-section').style.display = 'none';
            document.getElementById('todo-app').style.display = 'block';
            loadTasks();
        } else {
            alert('Falha no login');
        }
    });
});

function loadTasks() {
    fetch('/tasks', {
        headers: { 'Authorization': 'Bearer ' + accessToken }
    })
    .then(res => res.json())
    .then(data => {
        const taskList = document.getElementById('task-list');
        taskList.innerHTML = '';
        data.tasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = task.title;
            const completeBtn = document.createElement('button');
            completeBtn.textContent = 'Completar';
            completeBtn.addEventListener('click', () => updateTask(task._id));
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Remover';
            deleteBtn.addEventListener('click', () => deleteTask(task._id));
            li.appendChild(completeBtn);
            li.appendChild(deleteBtn);
            taskList.appendChild(li);
        });
    });
}

function addTask() {
    const title = document.getElementById('task-input').value;
    fetch('/tasks', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + accessToken
        },
        body: JSON.stringify({ title })
    })
    .then(res => res.json())
    .then(() => {
        document.getElementById('task-input').value = ''; // Limpa o campo de entrada
        loadTasks(); // Recarrega a lista de tarefas
    });
}

function updateTask(taskId) {
    fetch(`/tasks/${taskId}`, {
        method: 'PUT',
        headers: { 'Authorization': 'Bearer ' + accessToken }
    })
    .then(() => loadTasks()); // Recarrega as tarefas após atualizar
}

function deleteTask(taskId) {
    fetch(`/tasks/${taskId}`, {
        method: 'DELETE',
        headers: { 'Authorization': 'Bearer ' + accessToken }
    })
    .then(() => loadTasks()); // Recarrega as tarefas após deletar
}

document.getElementById('add-task-btn').addEventListener('click', addTask);

