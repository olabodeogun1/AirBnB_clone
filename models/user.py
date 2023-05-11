#!/usr/bin/python3
'''
User object model
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    A module for user information
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
