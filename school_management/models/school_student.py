# -*- coding: utf-8 -*-

import datetime
import pytz

from odoo import models, fields, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Students'

    _sql_constraints = [
        ('unique_register_no', 'unique (register_no)', 'Register no. is unique!')
    ]

    name = fields.Char(required=True)
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Other")], required=True)
    department_id = fields.Many2one("college.department", required=True)
    # , ondelete='restrict'
    register_no = fields.Char()
    class_name = fields.Char()
    section = fields.Char()
    dob = fields.Date()
    age = fields.Integer(compute="_compute_age")
    rank = fields.Integer(default=10)
    mark = fields.Float(default=100)
    doj = fields.Datetime("Date of Joining")
    description = fields.Text("About me")
    parent_ids = fields.Many2many('school.parent', ondelete='restrict')

    @api.model
    def create(self, values):
        print(values)
        values['register_no'] = self.env['ir.sequence'].next_by_code('school.student') or ('New')
        return super(SchoolStudent, self).create(values)

    @api.depends('dob')
    def _compute_age(self):
        today = datetime.datetime.today()
        # print(today)
        # print(datetime.datetime.now())
        # user_tz = self.env.user.tz or self.env.context.get('tz')
        # user_pytz = pytz.timezone(user_tz) if user_tz else pytz.utc
        # print(datetime.datetime.today().astimezone(user_pytz).replace(tzinfo=None))
        print("self")
        print(self)
        for record in self:
            print("record")
            print(record)
            if record.dob:
                age_calc = (datetime.datetime.today().date() - record.dob).days / 365
                print(age_calc)
                record.age = round(age_calc)
            else:
                record.age = 0
