# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char()
    active = fields.Boolean(default=True)
    college_department_id = fields.Many2one("college.department")
    hod_of_dept_id = fields.One2many("college.department", "hod_id")
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Other")], required=True)
    user_id = fields.Many2one("res.users")

    @api.onchange('college_department_id')
    def onchange_college_department_id(self):
        for record in self:
            print(record)
            print(record.college_department_id)
            record.user_id.college_department_id = record.college_department_id
