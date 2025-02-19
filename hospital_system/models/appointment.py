from odoo import api, models, fields


class Appointment(models.Model):
    _name = "hospital.appointment"
    _description = "hospital appointment class"
    _rec_name = "patient_name"

    patient_name = fields.Many2one("hospital.patient", string="Patient name")
    admitted = fields.Datetime(string="Admitted at")
    room_no = fields.Char(string="Room no.")
    pharmacy_line_ids = fields.One2many("appointment.pharmacy.line", "appointment_id", string="Pharmacy Lines")
    prescription = fields.Html("Prescription")

    def cancel_appointment(self):
        action = self.env.ref('hospital_system.action_hospital_cancel_appointment_view').read()[0]
        return action


class AppointmentLine(models.Model):
    _name = "appointment.pharmacy.line"
    _description = "Appointment pharmacy line"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(string="Price")
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
