"""
This module contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
