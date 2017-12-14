# -*- coding: utf-8 -*-
from odoo import _, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    customer = fields.Many2one('res.partner', domain=[('customer', '=', True)])
    
    sale_order = fields.Many2one('sale.order', string='Sale Order')