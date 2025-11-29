# Task Tracker CLI
My personal solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) problem on [Roadmap.sh](https://roadmap.sh/dashboard).

## Features
- Add, update, delete tasks (with optional complete-by dates and priorities)
- Mark tasks as in-progress or done
- List tasks with optional status filtering (todo, in-progress, done)
- JSON storage in `data/tasks.json`

## Key skills demonstrated
- Command-line UX: argparse subcommands plus an interactive REPL prompt.
- Data modeling: lightweight dataclass for tasks with defaults and serialization.
- Persistence: JSON file storage with safe creation/reset handling.
- Validation: flexible date parsing/formatting and priority normalization.
- User feedback: colored output, friendly prompts, and error messaging.

## Project layout
```text
TASK-TRACKER/
  task_cli.py
  data/
    tasks.json  # created automatically while running
  taskmanager/
    __init__.py
    storage.py
    models.py
    manage.py
  README.md
  LICENSE
```
