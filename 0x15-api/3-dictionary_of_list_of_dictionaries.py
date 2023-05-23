#!/usr/bin/python3
"""Dictionary of list of dictionaries"""


import json
import requests


def run():
    users = "https://jsonplaceholder.typicode.com/users/"
    todos_base = "https://jsonplaceholder.typicode.com/todos/?userId={}"

    employees = requests.get(users).json()

    data = {}
    for employee in employees:
        employee_id = employee.get("id")
        tasks = requests.get(todos_base.format(employee_id)).json()
        data[employee_id] = []
        for task in tasks:
            data[employee_id].append(
                {
                    "username": employee.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
            )

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    run()
