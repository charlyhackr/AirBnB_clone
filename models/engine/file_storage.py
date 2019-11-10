import json
"""
File Storage class.
"""


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

    def __init__(self):
        """ Initializes a FileStorage instance. """
        self.__objects = {}

    def all(self):
        return self.__objects
