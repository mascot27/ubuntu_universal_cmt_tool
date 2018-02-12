import json
from modules import module_directory


def create_all_directories(directoriesFile):

    with open(directoriesFile, 'r') as f:
        json_data = json.load(f)

    for element in json_data["directories"]:
        path = element["path"]

        owner_user = element["owner_user"]
        owner_group = element["owner_group"]
        mode = element["mode"]

        d = module_directory.Directory(path)
        print(path)
        print(d.create())

        if owner_user:
            if not owner_group:
                owner_group = None

            d.change_owner(owner_user, owner_group)

        if mode:
            d.change_permissions(mode)



