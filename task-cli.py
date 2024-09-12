import os
import sys
from jsondb import TaskDB

db = TaskDB("task-db.json")

def add(*args):
    db.add_task(*args)

command_map = {
    "add": add,
}

args = sys.argv[1:]
command_map[args[0]](*args[1:])