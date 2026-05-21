from datetime import datetime
# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []
# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    index = int(index)

    if index < 0 or index >= len(tasks):
        raise IndexError("Invalid task index.")

    tasks[index]["completed"] = True

    print("Task marked as complete!")



# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = []
    for task in tasks:
        if task["completed"] == False:
            pending.append(task)
    return pending
        


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)

    if total_tasks == 0:
        return 0

    completed_tasks = 0
    for task in tasks:
        if task["completed"] == True:
            completed_tasks += 1

    progress = (completed_tasks / total_tasks) * 100
    return progress
