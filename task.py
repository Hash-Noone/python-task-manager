class Task:
    """A task with a title that starts out incomplete."""

    def __init__(self, task):
        self.task = task
        self.completed = False

    def complete(self):
        self.completed = True

