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
     
    with open("{}.json".format(data), "w") as file_json:
        json.dump({data: [{"task": d.get("title"),
                               "completed": d.get("completed"),
                               "username": user_name} for d in todo]},
                  file_json)

if __name__ == "__main__":
    input_data = sys.argv[1]
    main(input_data)

