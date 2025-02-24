from odoo import api, fields, models


class SalesOrder(models.Model):
    _inherit = "sale.order"

    continent = fields.Selection([('asia', 'Asia'),
                                    ('africa', 'Africa'),
                                    ('europe', 'Europe'), ('australia', 'Australia'),
                                    ('north america', 'North America'),
                                    ('south america', 'South America'),
                                    ('antarctica', 'Antarctica')], string="Select continent")
