{
    'name': 'Hospital',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'base'
    ],

    'website': 'https://kitworks.systems/',
    'author': 'Kitworks Systems',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose.
    """,

    'data': [
        'security/ir.model.access.csv',

        'views/kw_hospital_menu.xml',
        'views/kw_hospital_doctor_views.xml'
    ],

    'application': True,
    'installable': True,

    'images': [
        'static/description/icon.png'
    ],
}
