import json
import requests

token = 'https://api.myjson.com/bins/855ss'

problems = requests.get(token)
problems = problems.json()
# print(r.json())

# with open('problems.json') as f:
#   data = json.load(f)


# To Print the json dict
# for key,val in problems.items():
#     print(key, "=>", val)
