from datetime import datetime

# Function to add a new task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ").strip()  # User inputs task description
    priority = input("Enter the priority (high, medium, low): ").strip().lower()  # Sets priority level
    deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()  # Sets task deadline

    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")  # Validates deadline format
        formated_date = deadline_date.strftime("%Y-%m-%d")

        now = datetime.now().date()  # Get today's date (YYYY-MM-DD)
        deadline_date_only = deadline_date.date()  # Extract only the date from the deadline

        if deadline_date_only < now:
            print("You cannot add a task for a day before the current day")
            return

        if task and priority in ["high", "medium", "low"]:
            todo_list.append({"task": task, "priority": priority, "deadline": formated_date})  # Adds task to list
            print(f"'{task}' with priority '{priority}' and deadline '{formated_date}' has been added to the list.")
        else:
            print("Invalid priority. Choose from high, medium, or low.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

