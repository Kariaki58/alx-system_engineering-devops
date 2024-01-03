#!/usr/bin/python3
"""export to json"""
import json
import sys
import requests


if __name__ == "__main__":
    sessionReq = requests.Session()

    id = sys.argv[1]
    todoid = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    username = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    getter = sessionReq.get(todoid)
    getteruser = sessionReq.get(username)

    json_req = getter.json()
    usr = getteruser.json()['username']

    taskData = []
    serizlided = {}

    for all_Emp in json_req:
        taskData.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    serizlided[id] = taskData

    file_Json = id + ".json"
    with open(file_Json, mode='w') as f:
        json.dump(serizlided, f)

