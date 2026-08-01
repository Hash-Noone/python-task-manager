from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. [{status}] {task.title}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)