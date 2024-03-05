from odoo import models, fields, api


class FleetCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight=fields.Float("max weight")
    max_volume=fields.Float("min weight")

    def _compute_display_name(self):
        for record in self:
            # record.display_name = str(record.id) + str(record.max_weight) + str(record.max_volume)
            record.display_name = f"{record.name} ({record.max_weight}kg,{record.max_volume}m3)"
