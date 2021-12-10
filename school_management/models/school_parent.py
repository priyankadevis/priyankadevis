# -*- coding: utf-8 -*-

import datetime
import pytz

from odoo import models, fields, api


class SchoolParent(models.Model):
    _name = 'school.parent'
    _description = 'School Parent'

    name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    address = fields.Char()
    dob = fields.Date()
    guardian = fields.Boolean()
    student_ids = fields.Many2many('school.student')
    # student_ids = fields.Many2many('school.student', 'parent_student_rel', 'parent_id', 'student_id')
