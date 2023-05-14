#!/usr/bin/python3
"""
File Storage model
"""
import json


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def set_file_path(self, path):
        '''
        Used to modify file path
        '''
        FileStorage.__file_path = path
        return FileStorage.__file_path

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        # from models.base_model.BaseModel import to_dict
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        import importlib
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        classes_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'State': State,
            'Amenity': Amenity,
            'Review': Review
        }
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as fp:
                jn_data = json.load(fp)
                for key, value in jn_data.items():
                    obj[key] = classes_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
