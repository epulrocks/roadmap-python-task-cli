import json
import time

class TaskDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.tasks = None
        self.__load_db()

    def __load_db(self):
        try:
            with open(self.db_path, "r") as f:
                json_dat = json.load(f)
                self.tasks = json_dat.get("tasks", {})
        except FileNotFoundError:
            self.tasks = {}
            self.__save_db()
    
    @staticmethod
    def __time_now():
        return time.time()

    def __save_db(self):
        with open(self.db_path, "w") as f:
            json.dump({"tasks": self.tasks}, f)

    def add_task(self, description, status = "todo"):
        acceptable_status = ["todo", "in progress", "done"]
        if status not in acceptable_status:
            raise ValueError(f"Invalid status: {status}. Acceptable values are: {acceptable_status}")
        now = self.__time_now()
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
        self.__save_db()
        print(f"Task added successfully (ID: {id})")
        return id
    
    def update_task(self, id, description):
        if id not in self.tasks:
            raise Exception(f"ID: {id} is not in database")
        now = self.__time_now()
        self.tasks[id]['description'] = description
        self.tasks[id]['updatedAt'] = now
        self.__save_db()
        print(f"Task updated successfully (ID: {id})")
        return id