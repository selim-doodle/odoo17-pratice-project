from odoo import api, models, fields

class CustomTeacher(models.Model):
    _inherit = 'school.teacher'

    home_town = fields.Char("Home district")
    
    def myFun(self):
        super(CustomTeacher, self).myFun()
        print("Hello from hslbd")