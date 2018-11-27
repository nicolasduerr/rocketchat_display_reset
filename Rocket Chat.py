import os, json

path = os.getenv('APPDATA')
print(path)

path = path + '\Rocket.Chat\window-state-main.json'
print(path)

with open(path, "r") as jsonFile:
    data = json.load(jsonFile)

data["x"] = 0
data["y"] = 0

with open(path, "w") as jsonFile:
    json.dump(data, jsonFile)
