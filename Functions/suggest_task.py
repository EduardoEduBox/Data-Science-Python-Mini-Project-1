from datetime import datetime

def get_current_time():
    """
    function that gets the current time and convert it to the right format for the get_current_day_period function

    :return: the integer of the current time
    """
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    return int(current_time)

def get_current_day_period(current_time):
    """
    Function that calculates the current day period based on the argument

    :param current_time: current time of the day
    :return: morning, afternoon, evening or day if statements are not satisfied
    """

    if current_time < 120000:
        return "morning"
    elif current_time < 180000:
        return "afternoon"
    elif current_time < 240000:
        return "evening"
    else:
        return "day"

def sort_by_date(my_list):
    """
    Function that sorts the list based on the date

    :param my_list: current list of dictionaries, [{"task": "", "priority": "high, medium or low", "deadline": "date"}]
    """

    my_list.sort(key=lambda task: int(task["deadline"].replace("-", '')))


def calculate_priority(current_list):
    """
    Function that sort the list based on the priority

    :param current_list: current list of dictionaries, [{"task": "", "priority": "high, medium or low", "deadline": "date"}]
    """

    if not current_list:
        return

    high_priority = []
    medium_priority = []
    low_priority = []

    for item in current_list:
        if item["priority"] == "high":
            high_priority.append(item)
        elif item["priority"] == "medium":
            medium_priority.append(item)
        elif item["priority"] == "low":
            low_priority.append(item)

    sort_by_date(high_priority)
    sort_by_date(medium_priority)
    sort_by_date(low_priority)

    return high_priority + medium_priority + low_priority


def suggest_tasks(todo_list):
    """
    Function that grabs a list, sort it and prints the list based on priority

    :param todo_list: current list of dictionaries, [{"task": "", "priority": "high, medium or low", "deadline": "date"}]
    """

    if len(todo_list) == 1:
        print(f"Good {get_current_day_period(get_current_time())}! You just have one task to work on: ")
        print(f"    {todo_list[0]["task"]} - {todo_list[0]["priority"]} - {todo_list[0]["deadline"]}")
        return

    prioritized_list = calculate_priority(todo_list)

    print(f"Good {get_current_day_period(get_current_time())}! Here are some tasks you might want to work on: ")
    for item in prioritized_list:
        print(f"    {item['task']} - {item["priority"]} - {item["deadline"]}")


# suggest_tasks([
#     {'task': "milk", 'priority': 'medium', 'deadline': '2020-01-01'},
#     {'task': "egg", 'priority': 'high', 'deadline': '2020-01-17'},
#     {'task': "juice", 'priority': 'low', 'deadline': '2020-04-01'},
#     {'task': "rice", 'priority': 'medium', 'deadline': '2020-07-18'},
#     {'task': "meat", 'priority': 'high', 'deadline': '2020-03-05'},
#     {'task': "nugget", 'priority': 'low', 'deadline': '2020-05-02'},
# ])
