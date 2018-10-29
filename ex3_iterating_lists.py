#!/usr/bin/env python3.7
users =  [
        {'admin': True, 'active': True, 'name': 'Paul'},
        {'admin': False, 'active': False, 'name': 'Fugazi'},
        {'admin': True, 'active': False, 'name': 'Lillie'},
        {'admin': False, 'active': True, 'name': 'Socks'},
        ]

line = 1

for user in users:
    prefix = f"{line}"

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "
    elif user['admin']:
        prefix += "(ADMIN)"

    print(prefix + user['name'])
    line += 1


