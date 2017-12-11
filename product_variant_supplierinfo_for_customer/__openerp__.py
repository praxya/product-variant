# -*- coding: utf-8 -*-
# © 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product customer info per variant',
    'summary': 'Customer info to product variant scope',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Tecnativa, Akretion, Rubén Cabrera (Praxya),'
              'Odoo Community Association (OCA)',
    'category': 'Product Management',
    'depends': [
        'product_supplierinfo_for_customer',
        'product_variant_supplierinfo',
    ],
    'data': [
        'views/product_product_view.xml',
        'views/product_supplierinfo_view.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
        'demo/procurement_demo.xml',
    ],
    'installable': True,
}
