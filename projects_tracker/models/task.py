from odoo import models, fields


class Task(models.Model):
    _name = 'project.task'
    _description = 'Task description'

    name = fields.Char(string='Task Name')
    time_required = fields.Integer(string="Required time(Hour)")
    project_id = fields.Many2one('project.project', string="Projects")
