import json, os
from pathlib import Path



# config_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '.', 'config', 'paths.json'))

#go 3 levels up from current file (needs to be adjusted when config.py is moved)
p = Path(__file__)
parts = p.parts[:-3]


for idx, step in enumerate(parts):

    if idx == 0:
        config_path = os.path.realpath(step)

    else:
        config_path = os.path.realpath(os.path.join(config_path, step))


#add location of config json
config_path = os.path.realpath(os.path.join(config_path, 'config', 'paths.json'))

print(config_path)

with open(config_path) as f:
   data = json.load(f)

f.close()

print(data)