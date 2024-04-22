#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
import sys


def get_employee_todo_progress(employee_id):
    # API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    # Extracting relevant information
    employee_name = todos[0]['name'].split()[0]
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    num_done_tasks = len(done_tasks)

    # Displaying information
    print(f"Employee {employee_name} is done with tasks({
        num_done_tasks}/{total_tasks}): ")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
