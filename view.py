import json

with open('problems.json') as f:
  data = json.load(f)

for key,val in data.items():
    print(key, "=>", val)
