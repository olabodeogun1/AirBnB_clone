#!/usr/bin/python3

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    '''
    Unit tests for the FileStorage class.
    '''

    def setUp(self):
        '''
        Set up method to initialize the FileStorage instance.
        '''
        self.storage = FileStorage()
        self.path = self.storage.set_file_path("test_save.json")

    def tearDown(self):
        '''
        Tear down method to reset the FileStorage instance.
        '''
        self.storage = None

    def test_all(self):
        '''
        Test the all() method of FileStorage.
        '''
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        '''
        Test the new() method of FileStorage.
        '''
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, self.storage.all())

    def test_save(self):
        '''
        Test the save() method of FileStorage.
        '''
        obj = BaseModel()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        self.path = self.storage.set_file_path("test_save.json")

        self.storage.save()

        with open(self.path, "r") as file:
            data = json.load(file)
            self.assertIn(obj_key, data)

    def test_reload(self):
        '''
        Test the reload() method of FileStorage.
        '''
        obj = BaseModel()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)

        filename = "test_reload.json"
        self.storage.__file_path = filename
        self.storage.save()

        self.storage.__objects = {}
        self.storage.reload()

        self.assertIn(obj_key, self.storage.all())

    def test_reload_file_not_found(self):
        '''
        Test the reload() method when the file is not found.
        '''
        self.filename = "nonexistent_file.json"
        self.storage.set_file_path(self.filename)
        self.output = self.storage.reload()

        self.assertEqual(self.output, None)


if __name__ == '__main__':
    unittest.main()
