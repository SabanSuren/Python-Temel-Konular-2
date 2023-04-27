# -*- coding: utf-8 -*-

import json

with open("jsonuser.json") as jsonuser:
    data=json.load(jsonuser)
    
    for x in range(6):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"],["street"])
        print(data[x]["address"],["street"],["geo"])
        
    