from email.policy import default

from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'
    _rec_name = 'project_title'

    project_title = fields.Char(string='Project Name', required=True)
    signed_at = fields.Date(string="Signed at")
    color = fields.Integer("Pic color")
    color2 = fields.Char("Pic color")
    project_line_ids = fields.One2many('project.project.line', 'project_id', string="Task lines")
    hide_required_time = fields.Boolean(default=False, string="Hide required time")

class ProjectProjectLine(models.Model):
    _name = "project.project.line"
    _description = "Project task line"
    _rec_name = 'task_id'

    task_id = fields.Many2one('project.task')
    assigned_date = fields.Date(string="Start date")
    required_time = fields.Integer(related="task_id.time_required", string="Required time")
    project_id = fields.Many2one('project.project', string="Projects")
