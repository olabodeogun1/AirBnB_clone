#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    Unit tests for the User class.
    '''

    def test_inheritance(self):
        '''
        Test if the User class inherits from the BaseModel class.
        '''
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes_initial_values(self):
        '''
        Test the initial values of the attributes.
        '''
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_attribute_types(self):
        '''
        Test the types of the attributes.
        '''
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
