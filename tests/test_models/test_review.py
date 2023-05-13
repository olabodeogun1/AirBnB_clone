#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    '''
    Unit tests for the Review class.
    '''

    def test_inheritance(self):
        '''
        Test if the Review class inherits from the BaseModel class.
        '''
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes_initial_values(self):
        '''
        Test the initial values of the attributes.
        '''
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_attribute_types(self):
        '''
        Test the types of the attributes.
        '''
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
