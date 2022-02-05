# -*- coding: utf-8 -*-

from odoo import fields, models


class AppointmentInfo(models.Model):
    _name = "appointment.info"
    _description = "Appointment Info"
    _rec_name = "patient_name"

    patient_name = fields.Char(required=True)
    physician = fields.Char()
    patient_status = fields.Char()
    appointment_date = fields.Datetime()
