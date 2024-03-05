{
    'name': "Transport Dispatch System",
    'version': '1.0',
    'depends': ['base', 'stock_picking_batch', 'fleet'],
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
        'views/fleet_batch_picking.xml'
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'data/estate_demo.xml',
    ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    # 'auto_install': False

}