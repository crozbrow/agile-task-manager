#serviço responsável por gerenciar as tarefas
#simula um pequeno CRUD em memória

tasks = []

def create_task(title, priority='Normal'):
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'priority': priority,
    }
    tasks.append(task)
    return task
def get_tasks():
    return tasks

def update_task(task_id, new_title):
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = new_title
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]