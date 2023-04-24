#!/usr/bin/python3
"""
Python script that, using the JSONPlaceholder API,
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        exit(1)

    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(api_url)
    todos = response.json()

    employee_name = todos[0]['name']
    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)
    completed_task_titles = [todo['title'] for todo in todos if todo['completed']]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for title in completed_task_titles:
        print("\t {} {}".format('\t', title))
