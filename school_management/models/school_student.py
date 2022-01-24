# -*- coding: utf-8 -*-

import datetime
import pytz

from odoo import models, fields, api, _


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Students'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _order = "sequence"

    _sql_constraints = [
        ('unique_register_no', 'unique (register_no)', 'Register no. is unique!')
    ]

    sequence = fields.Integer("Sequence", default=10)
    name = fields.Char(copy=False, tracking=True)
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Other")], required=True)
    college_department_id = fields.Many2one("college.department", required=True, tracking=True)
    # , ondelete='restrict'
    register_no = fields.Char()
    class_name = fields.Char()
    section = fields.Char()
    dob = fields.Date(tracking=True)
    age = fields.Integer(compute="_compute_age")
    rank = fields.Integer(default=10)
    fee = fields.Float(default=10000)
    mark = fields.Float(default=100)
    doj = fields.Datetime("Date of Joining")
    description = fields.Text("About me")
    parent_ids = fields.Many2many('school.parent', ondelete='restrict')
    state = fields.Selection([
        ('draft', 'Applied'),
        ('open', 'Confirmed'),
        ('done', 'Joined'),
        ('cancel', 'Cancelled')],
        string='Status', default='draft', copy=False, tracking=True)

    @api.model
    def create(self, values):
        print(values)
        values['register_no'] = self.env['ir.sequence'].next_by_code('school.student') or ('New')
        return super(SchoolStudent, self).create(values)

    def write(self, values):
        print(values)
        # values['name'] = 'Tintumon'
        return super(SchoolStudent, self).write(values)

    @api.depends('dob')
    def _compute_age(self):
        today = datetime.datetime.today()
        # print(today)
        # print(datetime.datetime.now())
        # user_tz = self.env.user.tz or self.env.context.get('tz')
        # user_pytz = pytz.timezone(user_tz) if user_tz else pytz.utc
        # print(datetime.datetime.today().astimezone(user_pytz).replace(tzinfo=None))
        for record in self:
            record.ensure_one()
            if record.dob:
                age_calc = (datetime.datetime.today().date() - record.dob).days / 365
                print(age_calc)
                record.age = round(age_calc)
            else:
                record.age = 0

    def button_search(self):
        self.ensure_one()
        print(self)
        search_ids = self.search([('gender', '=', 'male')], limit=30, offset=0, order='name asc')
        print(search_ids)
        print(search_ids.mapped('name'))
        # print('----------')
        # print(self.search([('id', 'in', [1, 2, 3, 4])]))
        # print(self.search_count([('id', 'in', [1, 2, 3, 4])]))
        # print(self.search_read([('id', 'in', [1, 2, 3, 4])]))
        # print('==============')
        # search_read_ids = self.search_read([('id', 'in', [1, 2, 3, 4, 10, 11])])
        # print(search_read_ids)
        # print('========!!!======')
        # for search_read in search_read_ids:
        #     print(search_read)
        #     print(search_read.get('sequence'))
        #     print(search_read['name'])
        #     print(search_read.get('test'))
        print('----------')
        browse_ids = self.browse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        print(browse_ids)
        filtered_ids = browse_ids.exists().filtered(lambda r: r.gender == self.gender)
        print(filtered_ids)
        print(filtered_ids.sorted(key=lambda r: r.name))
        print("-+-+0-----")
        print(filtered_ids.mapped('name'))
        print(filtered_ids.sorted(key=lambda r: r.name).mapped('name'))
        # for browse_id in browse_ids:
        #     print(browse_id)
        #     print(browse_id.id)
        #     print(browse_id.exists())
        #     print(browse_id.exists().name)
        # .exists()
        # print(self.copy())

    def copy(self, default=None):
        self.ensure_one()
        print(self)
        print(default)
        default = dict(default or {}, name=_('%s (copy)', self.name))
        return super(SchoolStudent, self).copy(default)

    # browse([1,2])
    # len([1,2]) = 2
    # school.student(1,2)
    # school.student(1)
    # school.student(2)
    # search() = school.student(1,2)
    # len(school.student(1,2)) =2
    # search_count() = 2
