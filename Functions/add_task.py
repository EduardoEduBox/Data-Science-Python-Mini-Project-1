from datetime import datetime

example_list = []

# Function to add a new task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ").strip()  # User inputs task description
    priority = input("Enter the priority (high, medium, low): ").strip().lower()  # Sets priority level
    deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()  # Sets task deadline
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")  # Validates deadline format
        formated_date = deadline_date.strftime("%Y-%m-%d")
        if task and priority in ["high", "medium", "low"]:
            todo_list.append({"task": task, "priority": priority, "deadline": formated_date})  # Adds task to list
            print(f"'{task}' with priority '{priority}' and deadline '{formated_date}' has been added to the list.")
        else:
            print("Invalid priority. Choose from high, medium, or low.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

add_task(example_list)

print(example_list)