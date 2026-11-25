"""Run the interactive task menu and save changes to disk."""

from storage import load_tasks, save_tasks
from task import Task
from task_manager import TaskManager

tasks = load_tasks()
task_manager = TaskManager(tasks)

while True:
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save and Exit")

    choice = input("Choose: ")

    match choice:
        case "1":
            title = input("Enter task title: ")
            if title.strip() == "":
                print("Task title cannot be empty.")
                continue
            task = Task(title)
            task_manager.add_task(task)
            print("Task added successfully.")
            save_tasks(task_manager.tasks)

        case "2":
            if not task_manager.tasks:
                print("No tasks available.")
            else:
                task_manager.view_tasks()

        case "3":
            # Menu task numbers start at 1; manager indexes start at 0.
            index = int(input("Enter task number to complete: ")) - 1
            if task_manager.complete_task(index):
                save_tasks(task_manager.tasks)
                print("Task completed.")
            else:
                print("Invalid task number.")


        case "4":
            index = int(input("Enter task number to delete: ")) - 1
            task_manager.delete_task(index)
            save_tasks(task_manager.tasks)
            print("Task deleted.")            

        case "5":
            save_tasks(task_manager.tasks)
            print("Tasks saved. Goodbye!")
            break

        case _:
            print("Invalid choice.")