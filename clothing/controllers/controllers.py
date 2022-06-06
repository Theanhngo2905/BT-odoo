# -*- coding: utf-8 -*-
# from odoo import http


# class Clothing(http.Controller):
#     @http.route('/clothing/clothing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clothing/clothing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clothing.listing', {
#             'root': '/clothing/clothing',
#             'objects': http.request.env['clothing.clothing'].search([]),
#         })

#     @http.route('/clothing/clothing/objects/<model("clothing.clothing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clothing.object', {
#             'object': obj
#         })
