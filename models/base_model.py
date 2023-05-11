#!/usr/bin/python3
""" Base model for all objects """

import uuid
from datetime import datetime


class BaseModel:
    """
    """
    def __init__(self):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        new_dict = self.__dict__.copy()
        new_dict.update({
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "created_at": self.created_at.isoformat()
        })
        return new_dict
