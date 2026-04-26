from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    stock_minimo = fields.Float(string="Stock Mínimo")

    alerta_stock = fields.Boolean(
        string="Alerta de Stock",
        compute="_compute_alerta_stock",
        store=True
    )

    @api.depends('qty_available', 'stock_minimo')
    def _compute_alerta_stock(self):
        for rec in self:
            rec.alerta_stock = rec.qty_available < rec.stock_minimo