
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean("Add stock transport",
        help="Add transport stock module")
    

    @api.onchange('module_stock_transport')
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        if self.module_stock_transport:
            self.env['ir.module.module'].sudo().search([('name', '=', 'stock_transport')]).button_immediate_install()
            self.module_stock_transport = True
