# -*- coding: utf-8 -*-

import json

data='{"firstname":"Saban","lastname":"Suren"}'

y=json.loads(data)

print(y["firstname"])
print(y["lastname"])


customer={
        "firstname":"ibrahim",
        "email":"ibrhmusta98@gmail.com"
        
        }
customerJson=json.dumps(customer)
print(customer)

print(json.dumps("Saban"))
