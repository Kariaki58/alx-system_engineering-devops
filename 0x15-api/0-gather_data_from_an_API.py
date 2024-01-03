#!/usr/bin/python3
"""gather data from an API"""
import json
import requests
import sys


def main(id):
    """main function"""
    todo_data = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    employee_name = user_data.json()["name"]
    count = 0
    completed = 0
    print(f"Employee {employee_name} is done with tasks ({completed}/{count}):")
    for data in todo_data.json():
        if data["userId"] == id:
            count += 1
        if data["completed"]:
            completed += 1
            print("\t{data[title]}")
    


if __name__ == "__main__":
    input_number = sys.argv[1]
    try:
        integer = int(input_number)
        main(integer)
    except TypeError:
        pass

