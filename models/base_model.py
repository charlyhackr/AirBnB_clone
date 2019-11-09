import uuid
from datetime import datetime
"""
base_model module, contains the BaseModel class
"""


class BaseModel():
    """
    BaseModel: Base Model class that contains an UUID, creation and
    modification dates.

    Attributes:
        id (uuid.UUID): Identifier of the model instance, consists in a UUID,
            version 4.
        created_at (datetime.datetime): creation date and time of the model
            instance.
        updated_at (datetime.datetime): update date and time of the model
            instance.
    """

    def __init__(self):
        """ Initializes a BaseModel instance. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of the object. """
        return "[BaseModel] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ Updates the instance update date. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ : returns a dictionary all keys/values of dict of the instance"""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        return ret_dict
