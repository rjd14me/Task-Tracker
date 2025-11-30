from datetime import datetime


class Task:
    def __init__(self, id, description, status="To Do", creation_date=None, due_date="No Due Date"):
        self.id = id
        self.description = description
        self.status = status
        # Keep a consistent string timestamp for JSON storage and display.
        self.creation_date = creation_date or datetime.now().isoformat()
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "creation_date": self.creation_date,
            "due_date": self.due_date,
        }
