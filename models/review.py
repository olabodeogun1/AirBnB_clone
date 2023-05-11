#!/usr/bin/python3
'''
Reviews module
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A module for managing customer reviews
    '''
    place_id = ''
    user_id = ''
    text = ''
