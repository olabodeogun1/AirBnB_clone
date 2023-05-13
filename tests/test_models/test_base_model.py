#!/usr/bin/python3

"""
unittest for base_model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init_with_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000',
            'updated_at': '2022-01-02T12:00:00.000',
            'name': 'Test Model'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2022, 1, 2, 12, 0, 0))
        self.assertEqual(model.name, 'Test Model')

    def test_init_without_kwargs(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, previous_updated_at)

    def test_to_dict_returns_valid_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_representation(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIn('BaseModel', model_str)
        self.assertIn(model.id, model_str)
        self.assertIn(str(model.__dict__), model_str)


if __name__ == '__main__':
    unittest.main()
