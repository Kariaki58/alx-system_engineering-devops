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

    sessionReq = requests.Session()
    
    employee = sessionReq.get(todo_id)
    employeeName = sessionReq.get(userid)

    response_json = employee.json()
    user_json = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in response_json:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = id + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in response_json:
            write.writerow([id, user_json, i.get('completed'), i.get('title')])
