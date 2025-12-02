#!/usr/bin/env python3

import requests
import sys
import json

usr_id = sys.argv[1]

url = f'https://jsonplaceholder.typicode.com/users/{usr_id}'
todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={usr_id}'

resp = requests.get(url)
cont = resp.json()
name = cont.get('name')

todo = requests.get(todo_url)
tasks = todo.json()

done_task = []
for task in tasks:
    if task.get('completed') == True:
        done_task.append(task)

print(f"Employee {name} is done with tasks ({len(done_task)}/{len(tasks)}):")

for task in done_task:
    print(f"\t {task.get('title')}")

filename = f"{usr_id}.json"
usr_list = []

for task in tasks:
    temp_dict = dict(task)
    del temp_dict['userId']
    del temp_dict['id']
    temp_dict['username'] = cont.get('username')
    usr_list.append(temp_dict)

usr_dict = {f"{usr_id}": usr_list}    


with open(filename, 'w', encoding='utf-8') as f:
    json.dump(usr_dict, f) 
