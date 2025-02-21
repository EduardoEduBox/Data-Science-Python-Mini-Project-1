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

