from odoo import api, models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'School student information'

    name = fields.Char(string="Student name")
    dob = fields.Date(string="Date of Birth")
    className = fields.Many2one('school.classroom', string="Class")