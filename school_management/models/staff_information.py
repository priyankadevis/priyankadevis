# -*- coding: utf-8 -*-

import datetime
import pytz

from odoo import models, fields, api


class StaffInformation(models.Model):
    _name = 'staff.information'
    _description = 'Staff Information'

    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    address = fields.Char()
