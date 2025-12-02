#!/usr/bin/env python3

import requests
import sys
import json


url = f'https://jsonplaceholder.typicode.com/users'
todo_url = f'https://jsonplaceholder.typicode.com/todos'

resp = requests.get(url)
cont = resp.json()

todo = requests.get(todo_url)
tasks = todo.json()

employees_tasks = {}
for usr in cont:
    usr_id = usr.get('id')
    usr_list = []
    for task in tasks:
        if task.get('userId') == usr_id:
            usr_dict = {'username': usr.get('username'),
                        'task': task.get('title'),
                        'completed': task.get('completed')
                        }
        usr_list.append(usr_dict)
    employees_tasks[usr_id] = usr_list

with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees_tasks, f)
