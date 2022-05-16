# -*- coding: utf-8 -*-
# from odoo import http


# class ViinLibraryManagent(http.Controller):
#     @http.route('/viin_library_managent/viin_library_managent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_library_managent/viin_library_managent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_library_managent.listing', {
#             'root': '/viin_library_managent/viin_library_managent',
#             'objects': http.request.env['viin_library_managent.viin_library_managent'].search([]),
#         })

#     @http.route('/viin_library_managent/viin_library_managent/objects/<model("viin_library_managent.viin_library_managent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_library_managent.object', {
#             'object': obj
#         })
