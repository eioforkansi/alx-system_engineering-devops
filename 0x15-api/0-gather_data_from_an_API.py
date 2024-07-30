#!/usr/bin/python3
"""
- Python script that returns information about his/her TODO list progress.
  Using REST API from https://jsonplaceholder.typicode.com/
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee ID>")
    else:
        try:
            employee_id = sys.argv[1]
            url = "https://jsonplaceholder.typicode.com"
            user_response = requests.get(f"{url}/users/{employee_id}")
            user_data = user_response.json()
            user_name = user_data["name"]

            task_response = requests.get(f"{url}/todos?userId={employee_id}")
            task_data = task_response.json()
            total_task = len(task_data)

            task_completed = []
            for task in task_data:
                if task["completed"]:
                    task_completed.append(task)
            print(f"Employee {user_name} is done with tasks" +
                  f"({len(task_completed)}/{total_task}):")
            for task in task_completed:
                print("\t " + task["title"])
        except Exception as error:
            print(f"Error: {error}")
