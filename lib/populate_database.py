import json

testing_dict = {
    "name" : "dhyan",
    "age" : "18",
    "city" : "chicago"
}

def populate():
    output = json.dumps(testing_dict)
    return output