#!/usr/bin/env python3.7

user = {'admin': True, 'active': False, 'name': 'Lillian'}

if user['admin'] and user['active']:
    print("ACTIVE - (ADMIN) " + user['name'])
elif user['active']:
    print("ACTIVE - " + user['name'])
elif user['admin']:
    print("(ADMIN) " + user['name'])
else:
    print(user['name'])


