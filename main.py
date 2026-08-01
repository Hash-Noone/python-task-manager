import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def get_task_index(tasks):
    try:
        return int(input("Enter the task number: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return -1

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "completed": False})
    print(f"Added task: '{task}'")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✓" if t["completed"] else "✗"
            print(f"{i}. [{status}] {t['task']}")

def complete_task(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    view_tasks(tasks)
    index = get_task_index(tasks)
    if not 0 <= index < len(tasks):
        print("Invalid task number.")
        return
    if tasks[index]["completed"]:
        print(f"Task '{tasks[index]['task']}' is already completed.")
    else:
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['task']}' marked as completed.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    view_tasks(tasks)
    index = get_task_index(tasks)
    if not 0 <= index < len(tasks):
        print("Invalid task number.")
        return
    deleted_task = tasks.pop(index)
    print(f"Task '{deleted_task['task']}' deleted.")


def main():
    tasks = load_tasks()

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
                add_task(tasks)
                save_tasks(tasks)
            case "2":
                view_tasks(tasks)
            case "3":
                complete_task(tasks)
                save_tasks(tasks)
            case "4":
                delete_task(tasks)
                save_tasks(tasks)
            case "5":
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()