"""Read and write tasks.json in the current working directory."""

import json
import os
from task import Task


def load_tasks():
    """Load task objects, or return an empty list if JSON is missing or invalid."""
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                data = json.load(f)

                tasks = []

                for item in data:
                    task = Task(item["title"])
                    task.completed = item["completed"]
                    tasks.append(task)

                return tasks

            except json.JSONDecodeError:
                return []

    return []


def save_tasks(tasks):
    """Overwrite the JSON file with the current task titles and statuses."""
    data = []

    data = [
    {
        "title": task.task,
        "completed": task.completed
    }
    for task in tasks
]

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)