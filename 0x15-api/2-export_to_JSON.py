#!/usr/bin/python3
"""Export to JSON"""


import json
import requests
import sys


def run():
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/" + user_id
    todos = "https://jsonplaceholder.typicode.com/todos/?userId=" + user_id

    employee = requests.get(user).json()
    tasks = requests.get(todos).json()

    data = {user_id: []}
    for task in tasks:
        data[user_id].append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username"),
            }
        )

    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run()
