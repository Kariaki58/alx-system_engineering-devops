#!/usr/bin/python3
"""gather data from an API"""
import json
import requests
import sys


def main(data):
    """main function"""
    base_url = "https://jsonplaceholder.typicode.com/"

    user_name = requests.get(base_url + "users/{}".format(data)).json()
    todo = requests.get(base_url + "todos", params={"userId": data}).json()

    tasks = [h.get("title") for h in todo if h.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_name.get("name"), len(tasks), len(todo)))
    [print("\t {}".format(i)) for i in tasks]


if __name__ == "__main__":
    data_in = sys.argv[1]
    main(data_in)
