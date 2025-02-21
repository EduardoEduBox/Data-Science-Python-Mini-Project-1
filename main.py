from functions.suggest_task import suggest_tasks
from functions.add_task import add_task
from functions.remove_task import remove_task
from functions.view_task import view_tasks

def print_menu():
    print("\nAdvanced To-Do List Application")
    print("   1. Add Task")  # Adds a task with priority and deadline
    print("   2. Remove Task")  # Removes a specific task from the list
    print("   3. View Tasks")  # Displays all tasks sorted by priority and deadline
    print("   4. Suggest Tasks")  # Suggests tasks based on urgency
    print("   5. Exit")  # Exits the application
    return int(input("Enter answer: "))

# Main function to run the application loop
def run_application():
    todo_list = []  # Initialize empty to-do list
    while True:
        choice = print_menu()
        try:
            if choice == 1:
                add_task(todo_list)  # Calls function to add task
                continue
            elif choice == 2:
                remove_task(todo_list)  # Calls function to remove task
                continue
            elif choice == 3:
                view_tasks(todo_list)  # Calls function to view tasks
                continue
            elif choice == 4:
                suggest_tasks(todo_list)  # Calls function to suggest urgent tasks
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break  # Exits the loop and ends program
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

run_application()