def view_tasks(todo_list):
    """
    Function to view all the tasks in the to-do list in a user-friendly format

    :param todo_list: current list of dictionaries, [{"task": "", "priority": "high, medium or low", "deadline": "date"}]
    :return: breaks the function if the list is empty
    """

    if not todo_list:
        print("You don't have item yet, try adding a task")
        return
    print("Here are all your items:")
    for i, item in enumerate(todo_list):
        print(f"    {i + 1}. {item["task"]} - {item["priority"]} - {item["deadline"]}")



# Function to remove a task from the to-do list
def remove_task(todo_list):
    if not todo_list:
        print("No tasks to remove.")
        return

    view_tasks(todo_list)  # Displays current tasks before removal
    try:
        index = int(input("Enter the task number to remove: ")) - 1  # User selects task number
        if 0 <= index < len(todo_list):
            removed_task = todo_list.pop(index)  # Removes task from list
            print(f"'{removed_task['task']}' has been removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

