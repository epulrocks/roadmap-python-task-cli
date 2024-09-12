import os
import sys
from jsondb import TaskDB

db = TaskDB("task-db.json")
args = sys.argv
print(db.tasks)
print(args)