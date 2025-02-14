from odoo import api, models, fields

class Patient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient class"

    name = fields.Char(string="Patient name")
    contact = fields.Char(string="Contact no.")