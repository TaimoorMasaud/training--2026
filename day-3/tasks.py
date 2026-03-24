#!/usr/bin/env python3
import json
import argparse
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path("tasks.json")


class Task:
    def __init__(self, id, title, status="todo", created_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()

    def complete(self):
        self.status = "done"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            status=data.get("status", "todo"),
            created_at=data.get("created_at")
        )


class TaskManager:
    def __init__(self, filepath=TASKS_FILE):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not self.filepath.exists():
            self.tasks = []
            return
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except (json.JSONDecodeError, IOError):
            print("Warning: tasks.json is corrupt or unreadable. Starting fresh.")
            self.tasks = []

    def save_tasks(self):
        with open(self.filepath, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title):
        new_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: [{task.id}] {task.title}")

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            task.complete()
            self.save_tasks()
            print(f"Task [{task.id}] marked as done.")
        else:
            print(f"Error: Task with id {task_id} not found.")

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task [{task.id}] deleted.")
        else:
            print(f"Error: Task with id {task_id} not found.")

    def list_tasks(self, filter=None):
        filtered = self.tasks
        if filter:
            filtered = [t for t in self.tasks if t.status == filter]
        if not filtered:
            print("No tasks found.")
            return
        for t in filtered:
            status_icon = "✔" if t.status == "done" else "✗"
            print(f"[{t.id}] {status_icon} {t.title} (Created: {t.created_at})")

    def _find_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Title of the task")

    # Complete task
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("id", type=int, help="ID of the task")

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("--filter", choices=["todo", "done"], help="Filter by status")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        manager.add_task(args.title)
    elif args.command == "done":
        manager.complete_task(args.id)
    elif args.command == "delete":
        manager.delete_task(args.id)
    elif args.command == "list":
        manager.list_tasks(filter=args.filter)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()