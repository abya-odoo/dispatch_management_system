from odoo import api, fields, models

class FleetDock(models.Model):
    _name='fleet.dock'

    name=fields.Char("name")