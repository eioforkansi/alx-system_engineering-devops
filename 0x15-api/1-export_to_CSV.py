#!/usr/bin/python3
"""
    1-export_to_CSV module
    take one arg the id number
    sends a get req to an api
    to get the name o user
    and all its task then export as csv file
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    usr = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    usr = requests.get(usr).json().get("username")
    todo = requests.get(todo).json()
    with open("{}.csv".format(id), "w+", newline='\n') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([id, usr, task.get("completed"),
                            task.get("title")])
