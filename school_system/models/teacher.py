from odoo import api, models, fields

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "School teacher model"

    name = fields.Char(string="Teacher name")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Select Gender")
    department = fields.Char(string="Department")
    active = fields.Boolean(string="Archived", default="False")