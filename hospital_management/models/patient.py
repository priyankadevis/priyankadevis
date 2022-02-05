# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _rec_name = "patient_name"
    _order = "age desc"

    patient_name = fields.Char(required=True)
    dob = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Other")], required=True)
    address = fields.Char()
    marital_status = fields.Char()
    blood_group = fields.Char()
    phn_no = fields.Char("Phone no.")
    appointment_date = fields.Datetime()
    appointment_end = fields.Datetime()
    delete = fields.Char()

    def name_get(self):
        res = []
        for record in self:
            if record.patient_name and record.age:
                res.append((record['id'], "%s@%s" % (record.patient_name, record.age)))
            elif record.patient_name:
                res.append((record['id'], "%s" % (record.patient_name)))
            else:
                res.append((record['id'], _("No Named Patient")))
        return res

    @api.constrains('appointment_date', 'appointment_end')
    def _check_appointment_date(self):
        today = fields.Date.today()
        now = fields.Datetime.now()
        for record in self:
            if record.appointment_date and record.appointment_end \
                    and record.appointment_end < record.appointment_date:
                raise ValidationError(_('The Appointment date must be before the Appointment end date'))
            if record.appointment_date and now > record.appointment_date:
                raise ValidationError(_('The Appointment date should be in the future'))
            if record.appointment_end and now > record.appointment_end:
                raise ValidationError(_('The end date should be in the future'))
