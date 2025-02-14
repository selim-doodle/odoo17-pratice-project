from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Project Name', required=True)
    signed_at = fields.Date(string="Signed at")
    task_ids = fields.One2many('project.task', 'project_id', string="Task lines")