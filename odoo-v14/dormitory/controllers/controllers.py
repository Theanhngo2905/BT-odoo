# -*- coding: utf-8 -*-
# from odoo import http


# class Dormitory(http.Controller):
#     @http.route('/dormitory/dormitory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dormitory/dormitory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dormitory.listing', {
#             'root': '/dormitory/dormitory',
#             'objects': http.request.env['dormitory.dormitory'].search([]),
#         })

#     @http.route('/dormitory/dormitory/objects/<model("dormitory.dormitory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dormitory.object', {
#             'object': obj
#         })
