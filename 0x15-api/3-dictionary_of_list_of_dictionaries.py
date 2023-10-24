#!/usr/bin/python3
"""
    Script based ont task 0 that export all data employees in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "/users").json()
    my_dict = {}
    for user in users:
        user_id = user.get("id")
        tasks = requests.get(url + "/todos?userId={}".format(user_id)).json()
        my_list = []
        for task in tasks:
            my_list.append({
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")})
        my_dict[user_id] = my_list

    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as file:
        json.dump(my_dict, file)
