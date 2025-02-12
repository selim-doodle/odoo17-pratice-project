from odoo import api, models, fields

class Assets(models.Model):
    _name = 'school.assets'
    _description = "School's assets"

    name = fields.Char(string="Assets' name")