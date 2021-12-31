# -*- coding: utf-8 -*-
{
    'name': "Agriculture Managements",
    'summary': """
        Agriculture Management summary of the module's purpose, """,
    'description': """
        Agriculture Management module's purpose

        Farmers (CRM)
            acre,
            experience in which farming varities,
            no. of farmers,
            own transportation/not
            farm location,
        Vendors (CRM),
            own transportation/not
            specific product,
            corporate/small scale
            
        Transportation/Logistics (Fleet),
            type of vehicle
            no. vehicle
        
        Finance(loan management- thirdparty),
            RBI Approved/Local financier,
            Loan interest percentage
            limit            
        
        Farm equipments(product),
            type of equipments/vehicles
            
        pesticide and fertilizer(product),
            varities,
            
        biofertilizer and methods to create biofertilizer,
            method in details(blog)
            are you selling(product)
            
        Warehouse/Godown management and its location(warehouse-stock),
            location
            rental
        
        Crop (product)
            * Crops type and subtypes
            * Crop circulation,
            * water management,  
            * Seeds,
            * Weed,
            Sales/buy/
        Weather report (need to developer),
            * integrate with any third party weather,
            * https://apps.odoo.com/apps/modules/15.0/agriculture_weather_records/
            * https://apps.odoo.com/apps/modules/10.0/user_weather_map/
        disease
            * minimising disease in crops to increase quantity or quality of harvest yield,
            * prevention
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/agriculture_crop_views.xml',
        'views/templates.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
