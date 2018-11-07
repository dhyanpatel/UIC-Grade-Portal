from lib.get_overall_grades import populate
import json
from pprint import pprint

with open('./lib/configuration.json', 'r+') as f:
    config = json.load(f)
    config["excel_file_path"] = "D:\\Personal Projects\\PycharmProjects\\CS141_GradeLookup\\static\\toUpload.xlsx"
    f.seek(0)
    json.dump(config, f, indent=4)
    f.truncate()