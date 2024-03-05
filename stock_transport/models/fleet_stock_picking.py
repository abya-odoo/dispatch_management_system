from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"
    
    volume = fields.Float(related='batch_id.batch_volume', store=True)
