{
    'name': 'Sale Purchase Link',
    'version': '19.0.1.0.0',
    'summary': 'Create Purchase Order directly from Sales Order',
    'category': 'Sales',
    'depends': ['sale', 'purchase'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
