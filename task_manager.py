from task import Task


class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError("Only Task instances can be added.")
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. [{status}] {task.task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            return True
        return False

    def delete_task(self, index):
        try:
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
            else:
                print("Invalid task number.")
        except TypeError:
            print("Enter task number.")
