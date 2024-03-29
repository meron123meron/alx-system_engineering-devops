#!/usr/bin/python3
"""using the url returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1].isdecimal() and int(argv[1]) >= 0:
            url = "https://jsonplaceholder.typicode.com/"
            user = requests.get(url + "users/{}".format(sys.argv[1])).json()
            todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

            completed = [t.get("title") for t in todos if t.get("completed") is True]
            print("Employee {} is done with tasks({}/{}):".format(
                user.get("name"), len(completed), len(todos)))
            for c in completed:
                print('\t {}'.format(c.get('title')))
