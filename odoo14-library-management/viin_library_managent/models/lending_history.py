'''
Created on May 16, 2022

@author: o0zero0o
'''

from odoo import models,fields,api

class LendingHistory(models.Model):
    _name="libary.management.category"
    _description='Lending History Model'
    name=fields.Char(required=True)
    description=fields.Char()
    
    