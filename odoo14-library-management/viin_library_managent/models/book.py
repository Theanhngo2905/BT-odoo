'''
Created on May 16, 2022

@author: o0zero0o
'''

from odoo import models,fields,api
from dateutil.utils import today


class Book(models.Model):
    _name='library.management.books'
    _description="Book Model"
    _rec_name="title"
    title=fields.Char(required=True,string="title")
    authors=fields.Many2many('libarary.management.author',string="Authors")
    categories=fields.Many2many('libary.management.category',string="Category")
    published_date=fields.Date(string='Published date')
    added_date=fields.Date(default=today(),readonly=1, string='Day add to Library: ')
    image=fields.Binary(string='Image')
    number_of_copy=fields.Integer(readonly=0,store=True)
     