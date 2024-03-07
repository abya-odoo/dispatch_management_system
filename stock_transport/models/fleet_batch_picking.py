from odoo import models, fields, api


class FleetBatchPicking(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('fleet.dock')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category')
    fleet_vehicle_id = fields.Many2one('fleet.vehicle')
    # batch_weight = fields.Float('Batch Weight', default=1)
    # batch_volume = fields.Float('Batch Volume', default=1)

    total_weight = fields.Float('Weight', compute='_compute_weight_and_volume', store=True)
    total_volume = fields.Float('Volume', compute='_compute_weight_and_volume', store=True)
    total_weight_percentage = fields.Float('Weight%', compute='_compute_weight_volume_percentage')
    total_volume_percentage = fields.Float('Volume%', compute='_compute_weight_volume_percentage')
 
    # driver_image = fields.Image(related='driver_id.image_1920')
    driver_image = fields.Image(related='fleet_vehicle_id.driver_id.image_1920')

    # fields for the transfer and lines  measure count picking_ids, move_line_ids
    transfer = fields.Integer("Transfer", compute='_compute_transfer_count', store=True)
    lines = fields.Integer("Lines", compute='_compute_lines_count', store=True)
    # volume = fields.Float(compute='_compute_volume')


    @api.depends('picking_ids')
    def _compute_transfer_count(self):
        for record in self:
            record.transfer = len(record.picking_ids)

    @api.depends('picking_ids')
    def _compute_lines_count(self):
        for record in self:
            record.lines = len(record.move_line_ids)

    @api.depends('picking_ids.weight','picking_ids.volume','move_line_ids')
    def _compute_weight_and_volume(self):
        for record in self:
            # print(record.batch_weight)
            weight_sum = 0
            volume_sum = 0
            for pack in record.picking_ids:
                weight_sum += pack.weight
                volume_sum += pack.volume
            record.total_weight = weight_sum
            record.total_volume = volume_sum
            print(record.total_volume) 
    
    @api.depends('picking_ids.weight','picking_ids.volume','move_line_ids')
    def _compute_weight_volume_percentage(self):
        for record in self:
            # print(record.batch_weight)
            weight_sum = 0
            volume_sum = 0
            for pack in record.picking_ids:
                weight_sum += pack.weight
                volume_sum += pack.volume
            if record.fleet_category_id.max_weight == 0:
                record.total_weight_percentage = weight_sum
            else:
                record.total_weight_percentage = (weight_sum/record.fleet_category_id.max_weight)*100

            if record.fleet_category_id.max_volume == 0:
                record.total_volume_percentage = volume_sum
            else:
                record.total_volume_percentage = (volume_sum/record.fleet_category_id.max_volume)*100


