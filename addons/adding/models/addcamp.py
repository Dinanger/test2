from odoo import models, fields, api

class adz (models.Model):
    
    _inherit = 'sale.order'



    test = fields.Char(string='prueba')

    