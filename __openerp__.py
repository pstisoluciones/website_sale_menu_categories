# -*- encoding: utf-8 -*-  
########################################################################################
#
#    Copyright (C) 2004-2016 OpenERP S.A. (<http://www.odoo.com>).
#    Copyright (c) 2016 Disgal Milladoiro, S.L. - Roberto Barreiro (<roberto@disgal.es>)
#
########################################################################################

{
    'name': 'eCommerce Menu Categories',
    'version': '9.0.1.4',
    'depends': [ 'website_sale',],
    'author': 'Roberto Barreiro',
    'website': 'https://bitbucket.org/disgalmilladoiro/',
    'summary': 'Product categories menu for website shop, mobile devices compatible',
    'description': '''
    Product categories menu pills for your website shop. It supports mobile devices. Includes a categories/subcategories navigation bar, and subcategories buttons.
    ''',
    'category': 'eCommerce',
    'data': [ 'views/website_sale_menu_categories.xml',],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': '19.99',
    'currency': 'EUR',
}
