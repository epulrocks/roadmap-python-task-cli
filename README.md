# CLI Task tracker (Python)

## Description
This is a practice project which was listed in roadmap.sh:
https://roadmap.sh/projects/task-tracker

Task tracker is a project used to track and manage your tasks using a simple command line interface (CLI).

## Project Goals
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- [x] Add, Update, and Delete tasks
- [x] Mark a task as in progress or done
- [x] List all tasks
- [x] List all tasks that are done
- [x] List all tasks that are not done
- [x] List all tasks that are in progress

Here are some constraints to guide the implementation:

- [x] You can use any programming language to build this project.
- [x] Use positional arguments in command line to accept user inputs.
- [x] Use a JSON file to store the tasks in the current directory.
- [x] The JSON file should be created if it does not exist.
- [x] Use the native file system module of your programming language to interact with the JSON file.
- [x] Do not use any external libraries or frameworks to build this project.
- [x] Ensure to handle errors and edge cases gracefully.

## Requirements
This project was build on Python 3.11.4. It is recommended to use the same version or at least any Python 3.11. Other version may work but never tested.

## Usage
The list of commands and their usage is given below:

Note: the "task-cli" command is only valid after you package the program into task-cli.exe using pyinstaller. To run using the python script, replace the command "task-cli" with "python task-cli.py" or "python3 task-cli.py" on linux.
```python
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Packaging into EXE file
To create the EXE file, we need to use pyinstaller.
1) install pyinstaller:
```console
pip install pyinstaller
```
or
install from requirements.txt (this will also install other libraries such as pytest):
```console
pip install -r requirements.txt
```

2) pack using pyinstaller:
```console
pyinstaller task-cli.spec
```