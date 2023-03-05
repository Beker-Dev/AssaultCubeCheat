import os
import json


def get_settings():
    file_name = 'cheat_values.json'

    if os.path.isfile(file_name):
        with open(file_name, 'r') as json_file:
            settings = json.load(json_file)
    else:
        settings = {
            "ammo": {
                "on": False,
                "amount": 20
            },
            "health": {
                "on": False,
                "amount": 100
            },
            "grenade": {
                "on": False,
                "amount": 3
            }
        }

        with open(file_name, 'w') as json_file:
            json.dump(settings, json_file, indent=4)

    return settings
