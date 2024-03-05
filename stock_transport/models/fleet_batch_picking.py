from odoo import models, fields, api


class FleetBatchPicking(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('fleet.dock')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category')
    fleet_vehicle_id = fields.Many2one('fleet.vehicle')
    # batch_weight = fields.Float('Batch Weight', default=1)
    # batch_volume = fields.Float('Batch Volume', default=1)

    total_weight = fields.Float('Weight', compute='_compute_weight_and_volume')
    total_volume = fields.Float('Volume', compute='_compute_weight_and_volume')
    driver_avatar = fields.Image(related='fleet_vehicle_id.driver_id.avatar_512')
    # volume = fields.Float(compute='_compute_volume')


    @api.depends('picking_ids')
    def _compute_weight_and_volume(self):
        for record in self:
            # print(record.batch_weight)
            weight_sum = 0
            volume_sum = 0
            for pack in record.picking_ids:
                print(pack.volume)
                print(pack.weight)
                weight_sum += pack.weight
                volume_sum += pack.volume
            if record.fleet_category_id.max_weight == 0:
                record.total_weight = weight_sum
            else:
                record.total_weight = (weight_sum/record.fleet_category_id.max_weight)*100
            if record.fleet_category_id.max_volume == 0:
                record.total_volume = volume_sum
            else:
                record.total_volume = (volume_sum/record.fleet_category_id.max_volume)*100


