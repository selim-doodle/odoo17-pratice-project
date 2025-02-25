from odoo import api, models, fields

class CustomTeacher(models.Model):
    _inherit = 'school.teacher'

    home_town = fields.Char("Home district")