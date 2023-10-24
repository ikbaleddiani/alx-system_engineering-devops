#!/usr/bin/python3
"""
Python script based ont task 0 that export data in CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    user = user.get("username")
    tasks = requests.get(url + "/todos?userId={}".format(user_id)).json()
    # Records format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    # Filaname format: USER_ID.csv
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            tuple = (user_id, user, task.get("completed"), task.get("title"))
            writer.writerow(tuple)
