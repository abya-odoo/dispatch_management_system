{
    'name': "My_Stock",
    'version': '1.0',
    'depends': ['base', 'stock'],
    'author': "Abhishek Name",
    'category': 'Stock',
    'description': """
    A stock module
    """,
    # data files always loaded at installation
    'data': [
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'data/estate_demo.xml',
        'views/res_config_settings.xml'
    ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    # 'auto_install': False

}