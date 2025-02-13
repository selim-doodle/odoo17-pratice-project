from odoo import api, models, fields


class ClassName(models.Model):
    _name = 'school.classroom'
    _description = 'School class model'
    _rec_name = 'class_name'

    class_name = fields.Char(string="Class Name", required=True, unique=True)
    no_of_capacity = fields.Integer(string="Student capacity")
    start_date = fields.Date(string="Class started at")

    _sql_constraints = [
        ('unique_class_name', 'UNIQUE(class_name)', 'Class Name must be unique!')
    ]
