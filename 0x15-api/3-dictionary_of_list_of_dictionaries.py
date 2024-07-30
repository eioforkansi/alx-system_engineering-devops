#!/usr/bin/python3
"""Write all employee data in json format to a file"""
from json import dump
import requests


def fetch_employee_data():
    """Get all task to be done by all employees"""
    employee_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    employees = requests.get(employee_url).json()
    todos = requests.get(todo_url).json()
    return employees, todos


def write_json(employees, todos):
    employee_dict = {}

    # Create a lookup dictionary for employee usernames
    user_lookup = {
            employee['id']: employee['username'] for employee in employees
    }

    for task in todos:
        user_id = task.get("userId")
        if user_id not in employee_dict:
            employee_dict[user_id] = []

        todo = {
            "username": user_lookup.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        employee_dict[user_id].append(todo)

    with open("todo_all_employees.json", "w") as json_file:
        dump(employee_dict, json_file, indent=4)


if __name__ == "__main__":
    employees, todos = fetch_employee_data()
    write_json(employees, todos)
