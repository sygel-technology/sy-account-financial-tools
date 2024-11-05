import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-sygel-technology-sy-account-financial-tools",
    description="Meta package for sygel-technology-sy-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_balance_zero',
        'odoo13-addon-account_move_line_due_date',
        'odoo13-addon-avoid_check_balanced_credit_debit',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
