from lib.get_overall_grades import populate
from pprint import pprint
import json

for x in json.loads(populate()):
    print(x)