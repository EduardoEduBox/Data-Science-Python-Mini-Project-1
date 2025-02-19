#To-do List Application - 2
from datetime import datetime

# Function to display the menu options to the user
def print_menu():
    print("\nAdvanced To-Do List Application")
    print("1. Add Task")  # Adds a task with priority and deadline
    print("2. Remove Task")  # Removes a specific task from the list
    print("3. View Tasks")  # Displays all tasks sorted by priority and deadline
    print("4. Suggest Tasks")  # Suggests tasks based on urgency
    print("5. Exit")  # Exits the application

# Function to add a new task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ").strip()  # User inputs task description
    priority = input("Enter the priority (high, medium, low): ").strip().lower()  # Sets priority level
    deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()  # Sets task deadline
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")  # Validates deadline format
        if task and priority in ["high", "medium", "low"]:
            todo_list.append({"task": task, "priority": priority, "deadline": deadline_date})  # Adds task to list
            print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")
        else:
            print("Invalid priority. Choose from high, medium, or low.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


