#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


if __name__ == "__main__":

    id = sys.argv[1]
    todo_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    username = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    response = requests.Session()
    employee = response.get(todo_id)
    employeeName = response.get(username)

    to_json = employee.json()
    username = employeeName.json()['username']

    emptylist = []
    serilized = {}

    for data in to_json:
        emptylist.append(
            {
                "task": data.get('title'),
                "completed": data.get('completed'),
                "username": username,
            })
    serilized[id] = emptylist

    json_file = id + "." + "json"
    with open(json_file, 'w') as file:
        json.dump(serilized, file)
