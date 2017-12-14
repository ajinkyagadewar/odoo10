# -*- coding: utf-8 -*-
# Copyright 2017 Vivi Liu
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "TPA System Enhanced",
    'description': """
        System customization for tpa""",
    'author': 'Vivi Liu',
    'website': "",
    'category': 'Custom',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'product', 'sale', 'purchase', 'stock', 'account', 'contacts'
    ],
    'data': [
        'security/tpa_menu_security.xml',
        'views/tpa_menu_views.xml',
        'views/webclient_templates.xml',
    ],
    'application': False,
}
