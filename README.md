# Python Task Manager

A command-line app for keeping a local to-do list. You can add, list,
complete, and delete tasks, and pick up where you left off the next time you run it.

## Requirements

- Python 3.10 or later (the menu uses `match`/`case`).
- No third-party packages are required.

## Run the app

From the repository directory, run:

```sh
python3 main.py
```

## Use the menu

| Option | Action |
| --- | --- |
| `1` Add Task | Enter a non-blank title to create a task. |
| `2` View Tasks | List numbered tasks. `✗` means incomplete and `✓` means complete. |
| `3` Complete Task | Enter the number shown next to the task to mark it complete. |
| `4` Delete Task | Enter the number shown next to the task to remove it. |
| `5` Save and Exit | Save the current list and close the app. |

For example, with an empty list, choose `1` and enter `Buy milk`. Choose `2`
to see `1. [✗] Buy milk`, then choose `3` and enter `1`. Choose `2` again to
see `1. [✓] Buy milk`, then choose `5` to exit.

## Project structure

| File | Role |
| --- | --- |
| `main.py` | Runs the interactive menu and handles user input. |
| `task.py` | Defines a task and its completion state. |
| `task_manager.py` | Adds, displays, completes, and deletes tasks in memory. |
| `storage.py` | Converts tasks to and from JSON. |

## Local storage

The app loads `tasks.json` from the current working directory on startup. If the
file does not exist, the app starts with an empty list. It writes the file when
you add, complete, or delete a task, and when you choose **Save and Exit**. Each
record contains a `title` and a `completed` boolean. Git ignores this local file.
