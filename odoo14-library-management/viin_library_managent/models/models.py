# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class viin_library_managent(models.Model):
#     _name = 'viin_library_managent.viin_library_managent'
#     _description = 'viin_library_managent.viin_library_managent'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
