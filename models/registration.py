from odoo import fields, models


class School(models.Model):
    _name = 'school.registration'
    _description = 'school'

    name = fields.Char('')