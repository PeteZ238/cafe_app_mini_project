main_menu_options = '''
Please select number of option to continue:
0: Exit App
1: View Product Options
2: View Courier Options
3: View Order Options
4: View Customer Options
5: View Settings Options'''

product_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Print product list
2: Add product to the menu
3: Update a product in the menu
4: Delete a product from the menu'''

courier_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Print courier list
2: Add courier to the list
3: Update a courier in the list
4: Delete a courier from the list'''

order_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Print orders
2: Create a new order
3: Amend an existing order
4: Cancel an order'''

customer_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Print customers
2: Add a customer
3: Update a customer
4: Delete a customer'''

settings_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Import products from csv
2: Import couriers from csv
3: Import customers from csv'''

order_print_options = '''
What orders would you like to see?
0: All active orders
1: All orders, including cancelled

Input:   '''

orders_sort_options = '''
How would you like to see the orders sorted by?
0: Order ID (default)
1: Order status
2: Courier

Input:   '''

product_update_options = '''
Please select the id of what you would like to update for this product:
0: Product name
1: Product price
2: Product stock

Input:   '''

courier_update_options = '''
Please select the id of what you would like to update for this courier:
0: Courier name
1: Courier phone

Input:   '''

customer_update_options = '''
Please select the id of what you would like to update for this customer:
0: Customer name
1: Customer address
2: Customer phone

Input:   '''

order_update_options = '''
Please select the id of what you would like to update for this order:
0: Customer
1: Products ordered
2: Courier
3: Order status

Input:   '''

order_by_options = ''''''

order_status_selection = '''Please select the id of the order status for this order.

Input:   '''

customer_selection = '''Please select the id of the customer you would like to add to the order.

Input:   '''

courier_selection = '''Please select the id of the courier you would like to add to the order.

Input:   '''

deletion_selection = '''Please select the id you would like to delete.

Input:   '''

update_selection = '''Please select the id you would like to update.

Input:   '''

input_statement = '\n' + '''What would you like to do?

Input:   '''

confirmation_statement = 'Are you certain you want to perform this action? [Y/N] '

does_not_exist = '\n' + 'The product you selected does not exist in the menu.'

does_exist = '\n' + 'The product you selected already exists in the menu.'

exit_statement = '\n' + 'Thank you, app now exiting!'

error_statement = '\n' + 'Invalid option, please select a valid option.'

success_statement = '\n' + 'Operation succesful!'