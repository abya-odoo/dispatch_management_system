from odoo import models, fields, api


class FleetBatchPicking(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('fleet.dock')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category')
    fleet_vehicle_id = fields.Many2one('fleet.vehicle')
    # batch_weight = fields.Float('Batch Weight', default=1)
    # batch_volume = fields.Float('Batch Volume', default=1)

    weight = fields.Float(compute='_compute_weight')
    volume = fields.Float('volume')
    driver_avatar = fields.Image(related='fleet_vehicle_id.driver_id.avatar_512')
    # volume = fields.Float(compute='_compute_volume')


    @api.depends('picking_ids')
    def _compute_weight(self):
        for record in self:
            # print(record.batch_weight)
            weight_sum = 0
            if record.fleet_category_id.max_weight == 0:
                record.fleet_category_id.max_weight = 100
            for pack in record.picking_ids:
                weight_sum += pack.weight
                # for stock_pick in pack:
                    # print('2')
            # print(weight_sum)
            record.weight = (weight_sum/record.fleet_category_id.max_weight)*100
            
                # if record.fleet_category_id.max_weight == 0:
                #     record.volume = 0;
                # else:
                #     record.volume = record.batch_volume/record.fleet_category_id.max_volume


