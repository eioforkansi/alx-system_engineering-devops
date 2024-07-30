#!/usr/bin/python3
"""Write all employee data in json format to a file"""
from json import dump
import requests
from sys import argv


def fetch_employee_data(id):
    """Get all task to be done by an employee"""
    employee = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    employee = requests.get(employee).json()
    employee_todo = requests.get(todo).json()
    return employee, employee_todo


def write_josn(id, employee, employee_todo):
    employee_dict = {id: []}

    for task in employee_todo:
        todo = {"task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")}
        employee_dict.get(id).append(todo)

        json_file_name = f"{id}.json"
        with open(json_file_name, "w") as json_file:
            dump(employee_dict, json_file)

    return employee_dict


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <id>")
        exit(1)

    id = argv[1]
    employee, employee_todo = fetch_employee_data(id)
    data = write_josn(id, employee, employee_todo)
