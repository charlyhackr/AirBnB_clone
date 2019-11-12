#!/usr/bin/python3
"""
This module contains the file storage class
"""
import json
import os


class FileStorage():
    """ Serializes class instances to JSON and deserializes in the other
        way around.

        Attributes:
            objects (dict): Dictionary containing the objects in the file
                storage, each member will be represented with its class name
                alongside its ID, separated with a period character.
            file_path (str): File path of the JSON file containing all the
                objects of the file storage.
    """
    __objects = {}
    __file_path = "storage.json"

    def all(self):
        """ Returns a dictionary with all the objects of the file storage. """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object inside the file storage. """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj.to_dict()

    def save(self):
        """ Saves the JSON of all the objects into the JSON storage file. """
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """ Reloads all its objects from the JSON storage file. """
        if (os.path.exists(self.__file_path) and
                os.path.isfile(self.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
