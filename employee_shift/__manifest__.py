# -*- coding: utf-8 -*-
###################################################################################
#
#    inteslar software trading llc.
#    Copyright (C) 2018-TODAY inteslar software trading llc (<https://www.inteslar.com>).
#
###################################################################################
{
    'name': "Employee shift rotation for Enterprise Edition",
    'version': '1.0',
    'category': 'HR',
    'price': 100.00,
    'currency': 'EUR',
    'maintainer': 'inteslar',
    'website': "https://www.inteslar.com",
    'license': 'OPL-1',
    'author': 'inteslar',
    'summary': 'Employee Shifts for enterprise edition By Inteslar',
    'images': ['static/images/main_screenshot.png'],
    'depends': ['resource', 'hr', 'hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_employee_shift_security.xml',
        'views/hr_employee_contract_view.xml',
    ],
    'installable': True,
    'application': True,
}