# -*- coding: utf-8 -*-
# Copyright 2017 Vivi Liu
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "TPA Application Enhanced",
    'description': """
        Application Customization for TPA""",
    'author': 'Vivi Liu',
    'website': "",
    'category': 'Custom',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'contacts', 'sale', 'purchase', 'stock', 'account', 'account_accountant'
    ],
    'data': [
        'views/tpa_product_views.xml',
        'views/tpa_sale_views.xml',
        'views/tpa_purchase_views.xml',
        'views/tpa_account_views.xml',
    ],
    'application': False,
}
