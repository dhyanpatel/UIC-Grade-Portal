from lib.get_overall_grades import populate
import json
from pprint import pprint
location = "./static/toUpload.xlsx"

x = populate(location)

pprint(json.loads(x))