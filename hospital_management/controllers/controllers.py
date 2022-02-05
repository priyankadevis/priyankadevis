# -*- coding: utf-8 -*-
from odoo import http


class HospitalManagement(http.Controller):
    @http.route('/hospital_management', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/hospital_management/json', type='json', auth='public')
    def list_json(self, **kw):
        print(kw)
        print(http.request)
        print(http.request)
        return http.request.env['hospital.patient'].search_read([])

    @http.route('/hospital_management/in/objects', type='http', auth='public')
    def list_in(self, **kw):
        return http.request.render('hospital_management.listing', {
            'root': '/hospital_management',
            'objects': http.request.env['hospital.patient'].search([]),
        })

    @http.route('/hospital_management/in/objects', auth='public')
    def list_in(self, **kw):
        return http.request.render('hospital_management.listing', {
            'root': '/hospital_management',
            'objects': http.request.env['hospital.patient'].search([]),
        })

    @http.route('/hospital_management/objects/<model("hospital.patient"):obj>', auth='public')
    def object(self, obj, **kw):
        print(obj)
        print(kw)
        return http.request.render('hospital_management.object', {
            'object': obj
        })
