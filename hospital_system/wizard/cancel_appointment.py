from odoo import api, models, fields


class CancelAppointmentWizard(models.TransientModel):
    _name = "hospital.appointment.cancel.wizard"
    _description = "Cancel Appointment Wizard"
    _rec_name = "appointment_id"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")