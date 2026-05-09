from odoo import models, fields, api
from odoo.exceptions import UserError

class StockMoveAutoFill(models.Model):
    _inherit = 'stock.move'




    auto_fill = fields.Boolean(string='Auto Fill', default=False)

    @api.onchange('auto_fill')
    def _onchange_auto_fill(self):
        if self.auto_fill:
            if not self.product_id:
                raise UserError("Please select a product before enabling Auto Fill.")
            # Set the quantity to the available stock for the product
            self.product_uom_qty = self.product_id.qty_available