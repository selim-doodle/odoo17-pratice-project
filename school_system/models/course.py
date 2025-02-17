from odoo import api, models, fields


class Course(models.Model):
    _name = "school.course"
    _description = "school course"
    _rec_name = "title"

    title = fields.Char(string="Course Title")
    duration = fields.Float(string="Duration in hour")
    capacity = fields.Integer(string="Max capacity")
    teacher_id = fields.Many2one('school.teacher')