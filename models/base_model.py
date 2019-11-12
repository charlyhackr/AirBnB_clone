#!/usr/bin/python3
"""
This module contains the BaseModel class for management.
"""
import uuid
from datetime import datetime
from models import storage


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

    def __init__(self, *args, **kwargs):
        """ Initializes a BaseModel instance.
           *args : Unused.
           **kwargs {dict}: key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    if isinstance(val, datetime):
                        setattr(self, key, val)
                    elif isinstance(key, str):
                        setattr(self,
                                key,
                                datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        pass
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            storage.new(self)

    def __str__(self):
        """ Returns the string representation of the object. """
        return "[BaseModel] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ Updates the instance update date. """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Returns a dictionary all keys/values of dict of the instance"""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        return ret_dict
