# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 12:02:31 2017

@author: Jacintha
"""

import xml.etree.cElementTree as ET
from collections import defaultdict


def get_user(element):
    if element.tag in ["node", "way", "relation"]:
        return element.attrib["uid"]
    else:
        return None

def get_all_users(filename):
    users = defaultdict(int)
    for _, element in ET.iterparse(filename):
        uid = get_user(element)
        if(uid not in users):
            if(uid):
                users[uid] += 1
    return users
    