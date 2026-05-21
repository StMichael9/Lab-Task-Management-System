from datetime import datetime

def validate_task_title(title):
    if not title:
        raise ValueError("Title cannot be empty.")  # raise valueError is like throw new Error() in JS
    if len(title) < 2:
        raise ValueError("Title must be at least 2 characters long.")


def validate_task_description(description):
    if not description:
        raise ValueError("Description cannot be empty.")
    if len(description) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    

def validate_due_date(due_date):
    if not due_date:
        raise ValueError("Due date cannot be empty.")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
