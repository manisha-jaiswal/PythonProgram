#JSON-JAVA SCRIPT OBJECT NOTATION

import json

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
