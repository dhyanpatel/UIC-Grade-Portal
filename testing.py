from lib.get_xlsx import create_xlsx

try:
    create_xlsx()
except TypeError:
    print("Missing PDF Path and/or API Key in setup.json")