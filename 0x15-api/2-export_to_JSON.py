#!/usr/bin/python3
''' send a get request for an api json and output in a fashioned and more
 readable format '''

if __name__ == "__main__":
    import json
    import sys
    import urllib.parse
    import urllib.request

    args = sys.argv
    no = int(args[1])
    user_todos = []
    todo_user = {}
    completed = 0
    completed_todos = []
    url = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
        all_todos = json.loads(the_page.decode('utf-8'))
    with urllib.request.urlopen(url_user) as response:
        users = json.loads(response.read().decode('utf-8'))
    for user in users:
        if user.get('id') == no:
            todo_user = user
    for todo in all_todos:
        if todo['userId'] == no:
            if todo['completed']:
                completed += 1
                completed_todos.append(todo)
            user_todos.append(todo)

    # export in json format
    array = []
    for todo in user_todos:
        array.append({"task": todo['title'], "completed": todo['completed'],
                      "username": todo_user['username']})
    with open('{}.json'.format(no), 'w') as f:
        json.dump({todo_user['id']: array}, f)
