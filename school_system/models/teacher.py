from odoo import api, models, fields
from .constants import GENDER_SELECTION

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "School teacher model"

    name = fields.Char(string="Teacher name")
    dob = fields.Date(string="Date of Birth")
    joined = fields.Date(string="Join date")
    gender = fields.Selection(GENDER_SELECTION, string="Select Gender")
    department = fields.Char(string="Department")
    active = fields.Boolean(string="Archived", default="False")
    course_ids = fields.One2many('school.course', 'teacher_id', string='Assigned courses')

    def myFun(self):
        print("Hello All! this is from school.teacher class")