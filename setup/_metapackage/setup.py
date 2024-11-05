import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-sygel-technology-sy-account-financial-tools",
    description="Meta package for sygel-technology-sy-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_balance_zero',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
