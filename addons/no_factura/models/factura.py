from odoo import models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_create_invoice(self):
        if not self.env.user.has_group('account.group_account_user'):
            raise UserError("No tienes permisos para facturar. Solo contabilidad puede hacerlo.")
        return super().action_create_invoice()