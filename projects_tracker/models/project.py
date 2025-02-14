from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Project Name', required=True)
    signed_at = fields.Date(string="Signed at")


class Task(models.Model):
    _name = 'project.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    time_required = fields.Integer(string="Required time(Hour)")
