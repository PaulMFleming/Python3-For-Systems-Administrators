#!/usr/bin/env python3.7

user = {'admin': True, 'active': True, 'name': 'Paul'}
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "
elif user['admin']:
    prefix = "(ADMIN)"

print(prefix + user['name'])


