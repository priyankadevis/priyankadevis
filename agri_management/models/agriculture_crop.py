# -*- coding: utf-8 -*-

from odoo import models, fields


class AgricultureCrop(models.Model):
    _name = 'agriculture.crop'
    _description = 'Agriculture Crop'

    crop_name = fields.Char(required=True)
    period_to_produce = fields.Char()
    starting_period = fields.Char()
    ending_period = fields.Char()
    crop_season = fields.Selection([('summer', "Summer"),
                                           ('rainy', "Rainy"),
                                           ('other', "Other")], required=True)
    crop_warehouse = fields.Char()
    crop_stock_location = fields.Char()
    disease=fields.Char()
    disease_cure=fields.Char()
    description = fields.Char()
