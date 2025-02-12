from odoo import api, models, fields

class AssetsCategory(models.Model):
    _name = 'school.assetscategory'
    _description = "Assets category"

    name = fields.Char(string="Category name")