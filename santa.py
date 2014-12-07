#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from urllib2 import urlopen
from itertools import izip


# Специально по заказу лука тянем случайные числа с random.org
def get_random(count):
    return urlopen('http://www.random.org/integers/?num='+str(count)+'&min=1&max=100&col=1&base=10&format=plain&rnd=new').read()[:-1].split('\n')

users = None
with open("users.json") as ufile:
    users = json.load(ufile)

valid = False
while( not(valid) ):
    valid = True
    relation_list = []
    users_with_random = izip(users, get_random(len(users)))
    randomized_users = sorted(users_with_random, key=lambda i:i[1])
    for (sender, target) in izip(users, map(lambda i:i[0], randomized_users)):
        if( sender['region_id'] == target['region_id'] ):
            valid = False
        else:
            relation_list.append( (sender, target) )

for (sender, target) in relation_list:
    print sender['name'], '->',  target['name']
