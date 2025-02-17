from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'
    _rec_name = 'project_title'

    project_title = fields.Char(string='Project Name', required=True)
    signed_at = fields.Date(string="Signed at")
    project_line_ids = fields.One2many('project.project.line', 'project_id', string="Task lines")


class ProjectProjectLine(models.Model):
    _name = "project.project.line"
    _description = "Project task line"
    _rec_name = 'task_id'

    task_id = fields.Many2one('project.task')
    assigned_date = fields.Date(string="Start date")
    project_id = fields.Many2one('project.project', string="Projects")
    required_time = fields.Integer(related="task_id.time_required", string="Required time")