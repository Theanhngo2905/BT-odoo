'''
Created on May 16, 2022

@author: o0zero0o
'''

from odoo import models,fields,api
from dateutil.utils import today

class BookRequest(models.TransientModel):
    _inherit='book'
    
    day_request=fields.date(default=today(),readonly=1)
    
    