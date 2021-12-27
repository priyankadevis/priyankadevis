# -*- coding: utf-8 -*-

import datetime
import pytz

from odoo import models, fields, api


class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'College Department'

    name = fields.Char("Department Name", required=True)
    hod_id = fields.Many2one("school.teacher", required=False)
    teacher_ids = fields.One2many("school.teacher", "department_id")
    student_ids = fields.One2many("school.student",  "department_id")
