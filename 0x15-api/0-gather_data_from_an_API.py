#!/usr/bin/python3
"""get a data from api"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """get employee todo progress"""
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()
    
    completed_tasks = [task['title'] for task in todo_data if task['completed']]
    
    print(f"Employee {user_data['name']}\
            is done with\
            tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
