from odoo import api, fields, models

class CustomTeacher(models.Model):
    _inherit = 'school.teacher'

    division = fields.Char("Division")