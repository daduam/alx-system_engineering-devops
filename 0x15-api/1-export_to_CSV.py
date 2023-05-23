#!/usr/bin/python3
"""Export to CSV"""


import csv
import requests
import sys


def run():
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/" + user_id
    todos = "https://jsonplaceholder.typicode.com/todos/?userId=" + user_id

    employee = requests.get(user).json()
    tasks = requests.get(todos).json()

    with open("{}.csv".format(user_id), "w") as f:
        writer = csv.writer(
            f,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL,
        )
        for task in tasks:
            writer.writerow(
                [
                    employee.get("id"),
                    employee.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run()
