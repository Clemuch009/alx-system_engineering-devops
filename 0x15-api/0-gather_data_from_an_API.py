#!/usr/bin/env python3

import sys
from urllib import request
import json

usr_id = sys.argv[1]

url = f'https://jsonplaceholder.typicode.com/users/{usr_id}'

with request.urlopen(url) as resp:
    body = resp.read().decode('utf-8')
    body = json.loads(body)
    name = body.get('name')

todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={usr_id}'

with request.urlopen(todo_url) as todo:
    todo = todo.read().decode('utf-8')
    tasks = json.loads(todo)

    task_done = []
    for task in tasks:
        if task["completed"] == True:
            task_done.append(task)
print(f"Employee {name} is done with tasks({len(task_done)}/{len(tasks)}):")

for task in task_done:
    print(f"\t{task.get('title')}")
