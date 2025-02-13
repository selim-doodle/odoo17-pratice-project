from odoo import api, models, fields

class Assets(models.Model):
    _name = 'school.section'
    _description = "Classroom's section"

    name = fields.Char(string="Section name")
    className = fields.Many2one('school.classroom')
