import json

class TaskDB:
    def __init__(self, db_path):
        self.db_path = db_path
        try:
            with open(self.db_path, "r") as f:
                jsondat = json.load(f)
                self.tasks = jsondat.get("tasks", {})
        except FileNotFoundError:
            self.tasks = {}
            self.save_db()        

    def save_db(self):
        with open(self.db_path, "w") as f:
            json.dump({"tasks": self.tasks}, f)