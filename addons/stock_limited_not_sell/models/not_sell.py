from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            for line in order.order_line:
                if line.product_id.stock_limited and line.product_uom_qty > line.product_id.qty_available:
                    raise UserError(_('No se puede confirmar la orden de venta porque el producto "%s" tiene stock limitado y no hay suficiente cantidad disponible.') % line.product_id.name)
        return super(ProductTemplate, self).action_confirm()