#!/usr/bin/python3
"""export to json"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    todo_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    username = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    sessionReq = requests.Session()

    response = sessionReq.get(todo_id)
    username = sessionReq.get(username)

    responses = response.json()
    usr = username.json()['username']

    alltask = []
    dictionary = {}

    for data in responses:
        alltask.append(
            {
                "task": data.get('title'),
                "completed": data.get('completed'),
                "username": usr,
            })
    dictionary[id] = alltask

    file_Json = id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(dictionary, f)
