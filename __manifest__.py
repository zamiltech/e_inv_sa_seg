# -*- coding: utf-8 -*-

{
    "name": "e-Invoice KSA - semaaljamal ",
    "version": "1.5",
    "depends": [
        'base', 'web', 'account',
    ],
    "author": "Mahmoud, Genius Valley",
    "category": "Accounting",
    "website": "https://micro-sl.com",
    "support": "odoo@micro-sl.com",
    "images": ["static/description/assets/main_screenshot.gif","static/description/assets/main_screenshot.png", "static/description/assets/ghits_desktop_inv.jpg",
               "static/description/assets/ghits_labtop1.jpg"],
    "price": "90$",
    "license": "OPL-1",
    "currency": "USD",
    "summary": "e-Invoice in Kingdom of Saudi Arabia KSA | tax invoice | vat  | electronic | e invoice | accounting | tax | free | ksa | sa |Zakat, Tax and Customs Authority | الفاتورة الضريبية | الفوترة  الالكترونية |   هيئة الزكاة والضريبة والجمارك",
    "description": """
    e-Invoice in Kingdom of Saudi Arabia updated for semat el gamal

    
    """
    ,
    "data": [
        "view/partner.xml",
        "view/company.xml",
        "report/base_document_layout.xml",
        "report/account_move.xml",
        "view/account_move_views.xml"

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    'assets': {
        'web.report_assets_common': [
            'einv_sa_seg/static/css/report_style.css',
        ],
    },
}
