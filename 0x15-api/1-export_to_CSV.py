#!/usr/bin/python3
"""
export to csv
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]
    todo_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    userid = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    response = requests.Session()

    todos = response.get(todo_id)
    user = response.get(userid)

    response_json = todos.json()
    user_json = user.json()['username']

    content = 0

    for data in response_json:
        if data['completed']:
            content += 1

    fileCSV = id + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in response_json:
            write.writerow([id, user_json, i.get('completed'), i.get('title')])
