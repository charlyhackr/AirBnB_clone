#!/usr/bin/python3
""" City. """
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ Class that inherits of  BaseModel."""

    state_id = ""
    name = ""
