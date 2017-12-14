# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields

import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = ['sale.order']
    
    project_name = fields.Char(string='Project Name', help="Specific project under under customer.")
    project_address = fields.Char(string="Project Address")
    project_spec = fields.Char(string="Project Specification")
    project_area = fields.Char(string="Project Area")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_bundled = fields.Boolean('Can be Grouped', readonly=True)
    
    product_spec = fields.Text(string="Product Specification")   
    product_remark = fields.Text(string="Product Remark")
    
    material_product_line = fields.One2many('material.product.line', 'order_line_id', string="Material Products")

    
class material_product_line(models.Model):
    _name = "material.product.line"

    order_line_id = fields.Many2one('product.template', 'Product Name')
    material_product_id = fields.Many2one('product.product', 'Product')
    material_product_spec = fields.Text(string='Product Specification')
    material_product_uom = fields.Many2one('product.uom', string='Unit of Measure')
    material_product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'))
    material_product_qty = fields.Float("Quantity")
    #material_product_currency_id = fields.Many2one(related='order_line_id.order_id.currency_id', store=True, string='Currency', readonly=True)
    material_product_price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)
    #material_product_price_tax = fields.Monetary(compute='_compute_amount_material', string='Taxes', readonly=True, store=True)
    #material_product_price_subtotal = fields.Monetary(compute='_compute_amount_material', string='Subtotal', readonly=True, store=True)
    #material_product_price_total = fields.Monetary(compute='_compute_amount_material', string='Total', readonly=True, store=True)
    material_product_tax_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    material_product_discount = fields.Float(string='Discount (%)', digits=dp.get_precision('Discount'), default=0.0)
    
    seq = fields.Integer('Sequence')
    '''
    @api.depends('material_product_uom_qty', 'material_product_price_unit', 'material_product_tax_id', 'material_product_currency_id')
    def _compute_amount_product_spec(self):
        """
        Compute the amounts of the material product line.
        """
        for line in self:
            
            price = line.material_product_price_unit * (1 - (line.material_product_discount or 0.0) / 100.0)
            taxes = line.material_product_tax_id.compute_all(price, line.material_product_currency_id, line.material_product_uom_qty, product=line.material_product_id, partner=line.order_line_id.order_id.partner_shipping_id)
            line.update({
                'material_product_price_tax': taxes['total_included'] - taxes['total_excluded'],
                'material_product_price_total': taxes['total_included'],
                'material_product_price_subtotal': taxes['total_excluded'],
            })
    '''        