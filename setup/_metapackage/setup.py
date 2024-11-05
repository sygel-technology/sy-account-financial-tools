import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-account-financial-tools",
    description="Meta package for sygel-technology-sy-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_move_line_due_date',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
