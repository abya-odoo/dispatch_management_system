from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float('volume', compute='_compute_volume')
    weight = fields.Float('Weight', compute='_compute_weight')

    @api.depends('move_ids', 'move_ids.move_line_ids.quantity')
    def _compute_volume(self):
        for record in self:
            for product in record.move_ids:
                record.volume += product.quantity*product.product_id.volume

    @api.depends('move_ids', 'move_ids.move_line_ids.quantity')
    def _compute_weight(self):
        for record in self:
            for product in record.move_ids:
                record.weight += product.quantity*product.product_id.weight
