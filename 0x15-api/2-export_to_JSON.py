#!/usr/bin/python3
"""
    Python script based ont task 0 that export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    user = user.get("username")
    tasks = requests.get(url + "/todos?userId={}".format(user_id)).json()

    my_list = []
    for task in tasks:
        my_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user})
    my_dict = {user_id: my_list}

    # Filaname format: USER_ID.json
    filename = "{}.json".format(user_id)
    with open(filename, 'w', newline='') as file:
        json.dump(my_dict, file)
