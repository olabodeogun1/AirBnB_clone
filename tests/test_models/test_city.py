#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''
    Unit tests for the City class.
    '''

    def test_inheritance(self):
        '''
        Test if the City class inherits from the BaseModel class.
        '''
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes_initial_values(self):
        '''
        Test the initial values of the state_id and name attributes.
        '''
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_attributes_types(self):
        '''
        Test the types of the state_id and name attributes.
        '''
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
