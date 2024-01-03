#!/usr/bin/python3
"""export to json"""
import json
import sys
import requests


def main(data):
    """main documentation"""
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(data)).json()
    user_name = users.get("username")
    todo = requests.get(base_url + "todos", params={"userId": data}).json()

    filename = data + ".json"
    with open(filename, mode="w") as file:
        json.dump({data: [{"task": d.get("title"),
                           "completed": d.get("completed"),
                           "username": user_name} for d in todo]}, file)

if __name__ == "__main__":
    input_data = sys.argv[1]
    main(input_data)

