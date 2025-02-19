tasks = {}

# adding a task using key, value pairs to make it easy to manage
def add_task(my_tasks):
    task_key = input("What is the name of your task? ")
    if task_key in my_tasks:
        print("You already have a task with that name!")
        return

    task_description = input("And What is its description? ")

    print(f"Task '{task_key}' successfully added!")

    my_tasks.update({task_key: task_description})

# checking if the item exists, if True, proceed to delete that item from the dict
def remove_task(my_tasks):
    if not my_tasks.keys():
        print("You don't have any tasks yet...")
        return

    keys = my_tasks.keys()
    formatted_keys = ', '.join(keys)
    task_remover_key = input(f"""Alright, which task would you like to remove?:
                (press "c" to cancel) 
            {formatted_keys}
            
    """)

    if task_remover_key == "c":
        return

    if task_remover_key in my_tasks:
        print(f"Task '{task_remover_key}' successfully deleted!")
        del my_tasks[task_remover_key]
    else:
        print("Please select a valid task. (check for typos or cases)")
        remove_task(my_tasks)

# simple getter function, retrieving all the values in a user-friendly format
def view_tasks(my_tasks):
    if not my_tasks.keys():
        print("You don't have any tasks yet...")
        return

    for key, item in my_tasks.items():
        print(f"Task: '{key}' Description: '{item}'")

# Add task when running the app for the first time
add_task(tasks)

# loop that will run this until the person exits the application
while True:
    action = int(input("""What would you like to do now?
                1 - Add another task
                2 - Remove an existing task
                3 - View all tasks
                4 - Exit application
    """))
    
    if action == 1:
        add_task(tasks)
        continue
    elif action == 2:
        remove_task(tasks)
        continue
    elif action == 3:
        view_tasks(tasks)
        continue
    elif action == 4:
        print("You exited")
        break
    else:
        print("Please enter a valid number!")
        continue