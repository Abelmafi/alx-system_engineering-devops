#!/usr/bin/python3
"""Request employee ID from API
"""
from json import dump
import requests
from sys import argv

if __name__ == "__main__":

    def make_request(resource, param=None):
        """Retrieve user from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # make request
        r = requests.get(url)

        # extract json response
        r = r.json()
        return r

    users = make_request('users')
    tasks = make_request('todos')

    # format before exporting

    export = {}
    for user in users:
        temp = []
        user_id = user['id']
        for task in tasks:
            if task['userId'] == user_id:
                temp.append({'username': user['username'],
                             'task': task['title'],
                             'completed': task['completed']})
        export[user_id] = temp

    with open('todo_all_employees.json', mode='w') as f:
        dump(export, f)
