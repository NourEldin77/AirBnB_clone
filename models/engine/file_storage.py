#!/usr/bin/python3
""" file_storge model """

import json


class FileStorage:
    """
    serializes instances to JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __obj_value = {}
    __instance_obj = {}
    def __init__(self):
        pass

    def all(self):
        """  returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
 


        FileStorage.__objects[
                f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        for key, obj_instance in FileStorage.__objects.items():
            FileStorage.__objects[key] = obj_instance.__cus__()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
