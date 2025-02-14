from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Project Name', required=True)
    task_ids = fields.One2many('project.task', 'project_id', string='Tasks')


class Task(models.Model):
    _name = 'project.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    project_id = fields.Many2one('project.project', string='Project', required=True)
