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
4: Cancel and delete an order'''

customer_menu_options = '''
Please select number of option to continue:
0: Return to main menu
1: Print customer list
2: Add customer to the list
3: Update a customer in the list
4: Delete a customer from the list'''

order_update_options = '''
Please select number of what you would like to update in the order:
0: Customer name
1: Customer address
2: Customer phone number
3: Products ordered
4: Courier
5: Order status'''

product_selection = '''PLease select the id of the products you would like to add to the order.
To select more than one items, please separate the index numbers with comma (,).'''

order_status_selection = '''Please select the id of the order status for this order: '''

customer_selection = '''Please select the id of the customer you would like to add to the order: '''

courier_selection = '''Please select the id of the courier you would like to add to the order: '''

deletion_selection = '''Please select the id you would like to delete: '''

update_selection = '''Please select the id you would like to update: '''

input_statement = '\n' + 'What would you like to do? '

confirmation_statement = 'Are you certain you want to perform this action? [Y/N] '

does_not_exist = '\n' + 'The product you selected does not exist in the menu.'

does_exist = '\n' + 'The product you selected already exists in the menu.'

exit_statement = '\n' + 'Thank you, app now exiting!'

error_statement = '\n' + 'Invalid option, please select a valid option.'

success_statement = '\n' + 'Operation succesful!'