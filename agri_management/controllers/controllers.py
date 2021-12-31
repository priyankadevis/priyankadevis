# -*- coding: utf-8 -*-
# from odoo import http


# class AgriManagement(http.Controller):
#     @http.route('/agri_management/agri_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agri_management/agri_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agri_management.listing', {
#             'root': '/agri_management/agri_management',
#             'objects': http.request.env['agri_management.agri_management'].search([]),
#         })

#     @http.route('/agri_management/agri_management/objects/<model("agri_management.agri_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agri_management.object', {
#             'object': obj
#         })
