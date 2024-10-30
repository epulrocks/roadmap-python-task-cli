import json
import time

class TaskDB:
    def __init__(self, db_path):
        self.db_path = db_path

    def __load(self):
        # Open json file, and load data from 'task' key
        try:
            with open(self.db_path, 'r') as f:
                json_dat = json.load(f)
                tasks = json_dat['tasks']
        # If file not found, return empty dict
        except FileNotFoundError:
            print(f'File "{self.db_path}" not found. Starting db with empty task list')
            tasks = {}
        except KeyError:
            print(f'File "{self.db_path}" not in expected format. Starting db with empty task list')
            tasks = {}
        return tasks
    
    def __save(self, tasks_data):
        with open(self.db_path, 'w') as f:
            json.dump({'tasks': tasks_data}, f)
    
    @staticmethod
    def __timenow():
        return time.time()
    
    @staticmethod
    def __status_isvalid(status):
        acceptable_status = ['todo', 'in-progress', 'done']
        if status not in acceptable_status:
            # Only accepts input from acceptable_status
            raise ValueError(f'Invalid status: {status}. Acceptable values are: {acceptable_status}')
    
    @staticmethod
    def __info_type_isvalid(info_type):
        acceptable_info_type = ['description', 'status']
        if info_type not in acceptable_info_type:
            # Only accepts input from acceptable_status
            raise ValueError(f'Invalid info_type: {info_type}. Acceptable values are: {acceptable_info_type}')

    def add_task(self, description):
        now = self.__timenow()
        tasks = self.__load()
        # Generate id from count of task
        id = len(tasks) + 1
        # Checking if id is already used, add 1 and recheck
        while id in tasks:
            id += 1
        id = str(id)
        new_task = {
            'description': description,
            'status': 'todo',
            'createdAt': now,
            'updatedAt': now
        }
        tasks[id] = new_task
        self.__save(tasks)
        return id
    
    def update_task(self, id, info_type, value):
        # Only used to update description
        self.__info_type_isvalid(info_type)
        if info_type=='status':
            self.__status_isvalid(value)
        tasks = self.__load()
        id = str(id)
        if id not in tasks:
            raise Exception(f'ID: {id} is not in database')
        now = self.__timenow()
        tasks[id][info_type] = value
        # Update 'updatedAt' to current time
        tasks[id]['updatedAt'] = now
        self.__save(tasks)
        return id
    
    def delete_task(self, id):
        tasks = self.__load()
        id = str(id)
        if id not in tasks:
            raise Exception(f'ID: {id} is not in database')
        del tasks[id]
        self.__save(tasks)
        return id
    
    def list_tasks(self, status_filter=None):
        if status_filter:
            self.__status_isvalid(status_filter)
        tasks = self.__load()
        output_string = lambda x, y: f"ID# {x}: {y['description']} - {y['status']}\nCreated: {y['createdAt']}\nUpdated: {y['updatedAt']}\n"
        for id, data in tasks.items():
            if status_filter:
                if data['status']==status_filter:
                    yield output_string(id, data)
            else:
                yield output_string(id, data)
