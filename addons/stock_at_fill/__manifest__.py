{
    'name': 'Stock at Fill',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'create buy order when the quantity got under 5.',
    'description': """
    This module automatically creates a purchase order when the stock quantity
     of a product falls below a specified threshold (e.g., 5 units). It helps ensure that inventory levels are maintained and prevents stockouts by triggering replenishment actions when necessary.
    """,
    'depends': ['base', 'stock' , 'purchase'],
    'data': [
        # XML files for views, actions, etc. can be added here
    ],
    'installable': True,


}