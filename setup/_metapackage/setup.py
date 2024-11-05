import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-financial-tools",
    description="Meta package for sygel-technology-sy-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_move_line_due_date>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
