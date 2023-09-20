#!/usr/bin/python3
"""Saves objects in file to FileStorage class attribute __objects"""
from models.engine.file_storage import FileStorage
from .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State

storage = FileStorage()
storage.reload()
