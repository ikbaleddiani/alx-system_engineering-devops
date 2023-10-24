#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id))
    user = user.json().get("name")
    tasks = requests.get(url + "/todos?userId={}".format(user_id)).json()
    total_tasks = len(tasks)
    tasks_done = [task for task in tasks if task.get("completed") is True]
    total_done = len(tasks_done)
    print("Employee {} is done with tasks({}/{}):".format(
        user, total_done, total_tasks))
    for task_done in tasks_done:
        print("\t {}".format(task_done.get("title")))
