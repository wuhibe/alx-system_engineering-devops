#!/usr/bin/python3
'''
module that uses REST api to return info on user's TODO and write to file
'''

import requests
import sys


def todojson():
    ''' function that gets todo tasks and exports data to json file '''
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    new = r.json()
    name = new.get('username')
    userid = new.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    new = r.json()
    size = len(new)
    stat = []
    task = []
    usertasks = []
    for i in range(0, size):
        stat.append(new[i].get('completed'))
        task.append(new[i].get('title'))
    for i in range(0, size):
        usertasks.append(dict([("task", "{}".format(task[i])),
                               ("completed", stat[i]),
                               ("username", "{}".format(name))]))
    final = dict([("{}".format(userid), usertasks)])
    with open("{}.json".format(userid), 'w') as f:
        f.write("{}".format(final))

if __name__ == "__main__":
    todojson()
