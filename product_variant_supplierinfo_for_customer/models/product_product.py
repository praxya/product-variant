# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# © 2016 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import api, models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    customer_ids = fields.One2many(
        comodel_name='product.supplierinfo', inverse_name='product_id',
        string='Customer', domain=[('type', '=', 'customer')])
    supplier_ids = fields.One2many(
        comodel_name='product.supplierinfo', inverse_name='product_id',
        string='Supplier', domain=[('type', '=', 'supplier')])

    tmpl_customer_ids = fields.Many2many(
        'product.supplierinfo',
        compute='_compute_customer_ids')
    tmpl_supplier_ids = fields.Many2many(
        'product.supplierinfo',
        compute='_compute_supplier_ids')

    variant_customer_ids = fields.One2many(
        'product.supplierinfo',
        'product_id')
    variant_supplier_ids = fields.One2many(
        'product.supplierinfo',
        'product_id')

    # TODO: Adapt seller fields to supplier/customer for variant:
    seller_delay = fields.Integer(
        related='seller_ids.delay',
        string='Supplier Lead Time',
        help=("This is the average delay in days between the purchase order "
              "confirmation and the receipts for this product and for the "
              "default supplier. It is used by the scheduler to order "
              "requests based on reordering delays."))
    seller_qty = fields.Float(
        related='seller_ids.qty',
        string='Supplier Quantity',
        help="This is minimum quantity to purchase from Main Supplier.")
    seller_id = fields.Many2one(
        related='seller_ids.name',
        relation='res.partner',
        string='Main Supplier',
        help="Main Supplier who has highest priority in Supplier List.")

    @api.multi
    def _compute_customer_ids(self):
        for product in self:
            customers = product.product_tmpl_id.customer_ids
            product.tmpl_seller_ids = customers.filtered(
                lambda x: not x.product_id)
            product.customer_ids = customers.filtered(
                lambda x: not x.product_id or x.product_id == product)

    @api.multi
    def _compute_supplier_ids(self):
        for product in self:
            suppliers = product.product_tmpl_id.supplier_ids
            product.tmpl_supplier_ids = suppliers.filtered(
                lambda x: not x.product_id)
            product.supplier_ids = suppliers.filtered(
                lambda x: not x.product_id or x.product_id == product)
