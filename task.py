class Task:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def complete(self):
        self.completed = True

