{
    'name': "Transport Dispatch System",
    'version': '1.0',
    'depends': ['base', 'stock_picking_batch', 'fleet', 'web_gantt'],
    'author': "Abhishek Name",
    'category': 'Fleet',
    'description': """
    A transport module
    """,
    # data files always loaded at installation
    'data': [
        # 'views/mymodule_view.xml',
        # 'security/estate_security.xml',
        # 'data/res.country.state.csv',
        'security/ir.model.access.csv',
        'views/fleet_model_view.xml',
        'views/fleet_batch_picking.xml',
        'views/fleet_stock_picking.xml',
        
    ],
    
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'data/estate_demo.xml',
    ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    # 'auto_install': False
    'license':'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_renderer.xml',
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_renderer.js',
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_view.js',
        ]
    }
}