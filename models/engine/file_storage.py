#!/usr/bin/python3

import json
import os

"""
"""


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                if os.stat(self.__file_path).st_size == 0:
                    return
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
