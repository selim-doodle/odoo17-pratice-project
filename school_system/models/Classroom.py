from odoo import api, models, fields


class ClassName(models.Model):
    _name = 'school.classroom'
    _description = 'School class model'
    _rec_name = 'className'

    className = fields.Selection(
        [('six', 'Six'), ('seven', 'Seven'), ('eight', 'Eight'), ('nine', 'Nine'), ('ten', 'Ten')], string="Class Name")
    no_of_capacity = fields.Integer(string="Student capacity")
