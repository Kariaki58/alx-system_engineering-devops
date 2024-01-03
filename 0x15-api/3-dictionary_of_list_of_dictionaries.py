#!/usr/bin/python3
""" Dictionary of list of dictionaries"""
import json
import requests


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    all_employees_tasks = {}

    for user_id in range(1, 11):
        todo = requests.get(base_url + "todos", params={"userId": user_id}).json()
        
        username = requests.get(base_url + "users", params={"id": user_id}).json()[0]["username"]
        user_tasks = []

        for task in todo:
            task_details = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.append(task_details)

        all_employees_tasks[str(user_id)] = user_tasks

    output_file = 'todo_all_employees.json'
    with open(output_file, 'w') as json_file:
        json.dump(all_employees_tasks, json_file)
