#!/usr/bin/python3
""" Review """
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class that inherits of BaseModel."""

    place_id = ""
    user_id = ""
    text = ""
