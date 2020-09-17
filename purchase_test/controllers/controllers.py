# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseTest(http.Controller):
#     @http.route('/purchase_test/purchase_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_test/purchase_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_test.listing', {
#             'root': '/purchase_test/purchase_test',
#             'objects': http.request.env['purchase_test.purchase_test'].search([]),
#         })

#     @http.route('/purchase_test/purchase_test/objects/<model("purchase_test.purchase_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_test.object', {
#             'object': obj
#         })
