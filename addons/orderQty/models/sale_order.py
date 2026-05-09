from odoo import models
from odoo.exceptions import UserError

class SaleOrder5(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):

        if not self.env.user.has_group('sales_team.group_sale_manager'):

            for order in self:
                for line in order.order_line:

                    if line.discount > 5.0:
                        raise UserError(
                            f"No puedes confirmar el pedido {order.name}. "
                            f"El producto '{line.product_id.name}' tiene un {line.discount}% de descuento. "
                            "Los descuentos mayores al 5% requieren validación de un gerente."
                        )

        return super().action_confirm()