#!/usr/bin/env python3

import requests
import sys
import csv

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

filename = f"{usr_id}.csv"

with open(filename, 'w', newline='', encoding='utf-8') as f:
    file = csv.writer(f, quoting=csv.QUOTE_ALL)
    for task in tasks:
        file.writerow([usr_id, cont.get('username'), task.get('completed'), task.get('title')])
