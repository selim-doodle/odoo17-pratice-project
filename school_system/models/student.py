from odoo import api, models, fields
from .constants import GENDER_SELECTION

class Student(models.Model):
    _name = 'school.student'
    _description = 'School student information'

    name = fields.Char(string="Student name")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(GENDER_SELECTION, string="Select gender")
    admission_date = fields.Date(string="Admission date")
    className = fields.Many2one('school.classroom', string="Class")