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
        FileStorage.__instance_obj = obj
        FileStorage.__obj_value = {key: value for key, value in obj.to_dict().items()}


        FileStorage.__objects[
                f"{obj.__class__.__name__}.{obj.id}"] = FileStorage.__obj_value
        

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """ 

        for key, value in FileStorage.__instance_obj.__dict__.items():
            if key not in FileStorage.__obj_value:
                FileStorage.__obj_value[key] = value

        obj_class_name = f"{FileStorage.__instance_obj.__class__.__name__}"
        name_format = f"{obj_class_name}.{FileStorage.__instance_obj.id}"

        FileStorage.__objects[f"{name_format}"] = FileStorage.__obj_value

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
