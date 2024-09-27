#!/usr/bin/python3
"""
This script retrieves and displays an employee's TODO list progress
from a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Define the API URLs
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_url = api_url + 'users/{}'.format(employee_id)
    todos_url = api_url + 'todos?userId={}'.format(employee_id)

    # Fetch user information (to get the employee's name)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    # Fetch todos information (to get the employee's tasks)
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found")
        sys.exit(1)

    # Parse JSON responses
    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Output the result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
