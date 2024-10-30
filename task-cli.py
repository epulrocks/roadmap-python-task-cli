from jsondb import TaskDB
import argparse
import sys

DB_PATH = 'task_db.json'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    update_parser = subparsers.add_parser("update", help="Update task description")
    update_parser.add_argument("task_id", help="Task ID to be updated")
    update_parser.add_argument("updated_description", help="New description")

    delete_parser = subparsers.add_parser("delete", help="Delete Task")
    delete_parser.add_argument("task_id", help="Task ID to be deleted")

    mark_inprogress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as 'in-progress'")
    mark_inprogress_parser.add_argument("task_id", help="Task ID to be updated")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as 'done'")
    mark_done_parser.add_argument("task_id", help="Task ID to be updated")

    list_parser = subparsers.add_parser("list", help="List out saved tasks")
    list_parser.add_argument("status_filter", nargs="?", help="Optional: filter list by status")

    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        exit(0)

    if args.command == 'add':
        id = TaskDB(DB_PATH).add_task(description=args.description)
        print(f"Task added successfully (ID: {id})")

    if args.command == 'update':
        id = TaskDB(DB_PATH).update_task(id=args.task_id,
                                         info_type='description',
                                         value=args.updated_description)
        print(f"Task (ID: {id}) description updated successfully")
    if args.command == 'delete':
        id = TaskDB(DB_PATH).delete_task(id=args.task_id)
        print(f"Task (ID: {id}) deleted successfully")
    if args.command == 'mark-in-progress':
        id = TaskDB(DB_PATH).update_task(id=args.task_id,
                                         info_type='status',
                                         value='in-progress')
        print(f"Task (ID: {id}) status changed to 'in-progress'")
    if args.command == 'mark-done':
        id = TaskDB(DB_PATH).update_task(id=args.task_id,
                                         info_type='status',
                                         value='done')
        print(f"Task (ID: {id}) status changed to 'done'")
    if args.command == 'list':
        task_lists = TaskDB(DB_PATH).list_tasks(status_filter=args.status_filter)
        for task in task_lists:
            print(task)