#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''
    Unit tests for the Amenity class.
    '''

    def test_inheritance(self):
        '''
        Test if the Amenity class inherits from the BaseModel class.
        '''
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attribute_initial_value(self):
        '''
        Test the initial value of the name attribute.
        '''
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_attribute_type(self):
        '''
        Test the type of the name attribute.
        '''
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
