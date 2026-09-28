import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# ==========================================================
# CORE FUNCTIONS
# ==========================================================
def add_task(title):
    """Add a new task with status='pending'."""
    tasks = load_tasks()
    new_id = 1 if not tasks else max(t["id"] for t in tasks) + 1
    today = "2026-09-28"   # will make it dynamic later
    
    task = {
        "id": new_id,
        "title": title,
        "status": "pending",
        "created_at": today,
        "updated_at": today
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"[ADDED] [{new_id}] {title}")


def list_tasks():
    """Print all tasks in a table."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one:")
        print('   python todo.py add "Your task"')
        return
    
    print()
    print("=" * 75)
    print(f"{'ID':<4} {'STATUS':<18} {'TITLE':<30} {'UPDATED':<12}")
    print("=" * 75)
    for task in tasks:
        title = task["title"]
        if len(title) > 28:
            title = title[:26] + ".."
        print(f"{task['id']:<4} {task['status']:<18} {title:<30} {task['updated_at']:<12}")
    print("=" * 75)
    print(f"Total: {len(tasks)}")
    print()

def update_status(task_id, new_status):
    """Update the status of a task by ID."""
    tasks = load_tasks()
    today = "2026-09-28"
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updated_at"] = today
            save_tasks(tasks)
            print(f"[UPDATED] [{task_id}] {task['title']} → {new_status}")
            return
    print(f"[ERROR] Task ID {task_id} not found.")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"[ERROR] Task ID {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"[DELETED] [{task_id}]")


def clear_done():
    """Remove all completed tasks."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["status"] != "done"]
    removed = len(tasks) - len(new_tasks)
    save_tasks(new_tasks)
    print(f"[CLEARED] {removed} done task(s) removed.")

# ==========================================================
# CLI
# ==========================================================
def print_help():
    print("""
CLI To-Do App
=====================================================
  python todo.py add "task title"      Add a new task
  python todo.py list                  Show all tasks
  python todo.py start <id>            Mark as in_progress
  python todo.py pause <id>            Mark as need_more_time
  python todo.py done <id>             Mark as done
  python todo.py delete <id>           Delete a task
  python todo.py clear                 Remove all done tasks
  python todo.py help                  Show this help
""")


def main():
    import sys
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print('[ERROR] Usage: python todo.py add "task title"')
            return
        add_task(" ".join(sys.argv[2:]))

    elif command == "list":
        list_tasks()

    elif command == "start":
        update_status(int(sys.argv[2]), "in_progress")

    elif command == "pause":
        update_status(int(sys.argv[2]), "need_more_time")

    elif command == "done":
        update_status(int(sys.argv[2]), "done")

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    elif command == "clear":
        clear_done()

    elif command in ("help", "-h", "--help"):
        print_help()

    else:
        print(f"[ERROR] Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()