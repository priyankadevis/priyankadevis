# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'summary': """
        School Management summary of the module's purpose, used as
        subtitle on modules listing""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/data.xml',
        'views/college_department_views.xml',
        'views/school_student_views.xml',
        'views/school_parent_views.xml',
        'views/school_teacher_views.xml',
        'views/staff_information_views.xml',
        'views/templates.xml',
    ],
    'license': 'LGPL-3',
    'application': True,
}
