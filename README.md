# CLI To-Do App

A command-line task manager built in Python. Tasks are stored in a JSON file with support for multiple statuses.

## Features

- Add tasks with custom titles
- Track task status: `pending`, `in_progress`, `need_more_time`, `done`
- List all tasks in a formatted table
- Update status with dedicated commands (`start`, `pause`, `done`)
- Delete individual tasks
- Clear all completed tasks
- Persistent storage using JSON

## Tech Stack

- Python 3
- JSON for data storage
- `os`, `json`, `sys` modules

## How to Run

```bash
# Add a new task
python todo.py add "Learn RAG"

# List all tasks
python todo.py list

# Mark task as in-progress
python todo.py start 1

# Mark task as done
python todo.py done 1

# Mark task as need_more_time
python todo.py pause 1

# Delete a task
python todo.py delete 2

# Clear all done tasks
python todo.py clear

# Show help
python todo.py help
```

## Status Meanings

| Status | Meaning |
|---|---|
| `pending` | Not started yet |
| `in_progress` | Currently working on it |
| `need_more_time` | Postponed for now |
| `done` | Completed |

## What I Learned

- File I/O with `with` statement
- JSON serialization and deserialization
- CLI argument parsing with `sys.argv`
- Functions, parameters, and return values
- List comprehensions and generator expressions
- Conditional logic with `if/elif/else`
- Status-based state management

## Author

Ankit Goswami — Gen AI Engineer Journey (2026)