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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
