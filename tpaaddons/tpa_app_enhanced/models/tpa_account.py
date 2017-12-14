# -*- coding: utf-8 -*-
from odoo import _, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    customer = fields.Many2one('res.partner', domain=[('customer', '=', True)])
    sale_order = fields.Many2one('sale.order', string='Sale Order')
    supplier_delivery_order = fields.Char(string='Supplier Delivery Order')