#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """state class that inherits from basemodel
    Args:
        name(str): user's name, empty string
    """
    name = ""
