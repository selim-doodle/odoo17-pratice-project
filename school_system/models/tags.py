from odoo import api, models, fields


class Tag(models.Model):
    _name = "school.tag"
    _description = "School tag"
    _rec_name = "tag_title"

    tag_title = fields.Char("Tag title")
    color = fields.Integer("Pic color")
