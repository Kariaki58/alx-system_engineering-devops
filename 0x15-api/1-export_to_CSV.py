#!/usr/bin/python3
"""export json to csv"""
import csv
import json
import requests
import sys


def main(data):
    """main documentation"""
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(data)).json()
    user_name = users.get("username")
    todo = requests.get(base_url + "todos", params={"userId": data}).json()

    with open("{}.csv".format(data), mode="w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([data, task['userId'],
                             task['completed',
                            task['title']]])


if __name__ == "__main__":
    input_data = sys.argv[1]
    main(input_data)
