#!/usr/bin/python3
"""export to json"""
import json
import requests
import sys


def main(data):
    """main documentation"""
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(data)).json()
    user_name = users.get("username")
    todo = requests.get(base_url + "todos", params={"userId": data}).json()

    filename = data + ".json"
    with open(filename, "w") as file:
        json.dump({data: [{"task": h.get("title"),
                               "completed": h.get("completed"),
                               "username": user_name} for h in todo]},
                  file)

if __name__ == "__main__":
    input_data = sys.argv[1]
    main(input_data)

