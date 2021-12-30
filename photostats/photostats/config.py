import json, os
from pathlib import Path


def read_config_var(var_name):


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

    #load JSON
    with open(config_path) as f:
        data = json.load(f)

    f.close()

    return data.get(var_name)



