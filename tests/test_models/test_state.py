#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    '''
    Unit tests for the State class.
    '''

    def test_inheritance(self):
        '''
        Test if the State class inherits from the BaseModel class.
        '''
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attribute_initial_value(self):
        '''
        Test the initial value of the name attribute.
        '''
        state = State()
        self.assertEqual(state.name, '')

    def test_attribute_type(self):
        '''
        Test the type of the name attribute.
        '''
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
