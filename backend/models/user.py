#!/usr/bin/env python3
'''
User entity module
'''
from app import db


class User(db.Model):
    '''User model class'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    events = db.relationship('Event', backref='user', lazy=True )
    
    @property
    def full_name(self):
        '''Retuns the full name dictionary'''
        return {
            'firstname': self.first_name,
            'lastname': self.last_name
        }
