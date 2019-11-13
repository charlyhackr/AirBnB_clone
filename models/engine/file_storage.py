#!/usr/bin/python3
"""
This module contains the file storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    __classes = {
        "BaseModel": lambda values: BaseModel(**values),
        "User": lambda values: User(**values),
        "State": lambda values: State(**values),
        "City": lambda values: City(**values),
        "Amenity": lambda values: Amenity(**values),
        "Place": lambda values: Place(**values),
        "Review": lambda values: Review(**values)
    }

    def all(self):
        """ Returns a dictionary with all the objects of the file storage. """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new object inside the file storage. """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ Saves the JSON of all the objects into the JSON storage file. """
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            f.write(json.dumps({key: value.to_dict() for (key, value) in
                                FileStorage.__objects.items()}))

    def reload(self):
        """ Reloads all its objects from the JSON storage file. """

        if (os.path.exists(self.__file_path) and
                os.path.isfile(self.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())

            for key, value in FileStorage.__objects.items():
                if '__class__' in value:
                    if value['__class__'] in FileStorage.__classes:
                        FileStorage.__objects[key] = FileStorage.__classes[
                            value['__class__']](value)
