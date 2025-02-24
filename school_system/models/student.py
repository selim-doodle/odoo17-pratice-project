from odoo import api, models, fields
from .constants import GENDER_SELECTION


class Student(models.Model):
    _name = 'school.student'
    _description = 'School student information'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Student name", tracking=True)
    profile_pic = fields.Image("Upload Image")
    dob = fields.Date(string="Date of Birth")
    regular = fields.Boolean("Regular")
    gender = fields.Selection(GENDER_SELECTION, string="Select gender")
    admission_date = fields.Date(string="Admission date")
    image = fields.Image(string="Add Image")
    className = fields.Many2one('school.classroom', string="Class")
    tag_ids = fields.Many2many('school.tag', string="Select tags")
    ref = fields.Char("Reference")


    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('school.student.sequence')
        return super(Student, self).create(vals)