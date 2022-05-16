'''
Created on May 16, 2022

@author: o0zero0o
'''


from odoo import models,fields,api


class Author(models.Model):
    _name='library.management.books'
    _description="Library Model"
    name=fields.Char(required=True)
    dob=fields.Date()
    
    