import json
import time

class TaskDB:
    def __init__(self, db_path):
        self.db_path = db_path
        try:
            with open(self.db_path, "r") as f:
                json_dat = json.load(f)
                self.tasks = json_dat.get("tasks", {})
        except FileNotFoundError:
            self.tasks = {}
            self.save_db()        

    def save_db(self):
        with open(self.db_path, "w") as f:
            json.dump({"tasks": self.tasks}, f)

    def add_task(self, description, status = "todo"):
        acceptable_status = ["todo", "in progress", "done"]
        if status not in acceptable_status:
            raise ValueError(f"Invalid status: {status}. Acceptable values are: {acceptable_status}")
        now = time.time()
        id = len(self.tasks) + 1
        while id in self.tasks:
            id += 1
        new_task = {
            "description": description,
            "status": status,
            "createdAt": now,
            "updatedAt": now
        }
        self.tasks[id] = new_task
        self.save_db()
        print(f"Task added successfully (ID: {id})")
        return id