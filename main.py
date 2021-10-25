import modules.print_statements as print_statements
import modules.support_functions as support_functions
import file_handlers.sql_module as sql

def main():
    '''Method that calls the main menu of the app.'''
    support_functions.clear()
    print(print_statements.main_menu_options)
    try:
        main_menu_input = int(input(print_statements.input_statement))
        if main_menu_input == 0:
            support_functions.clear()
            print(print_statements.exit_statement)
            quit()
        elif main_menu_input == 1:
            support_functions.clear()
            return product_menu()
        elif main_menu_input == 2:
            support_functions.clear()
            return courier_menu()
        elif main_menu_input == 3:
            support_functions.clear()
            return order_menu()
        elif main_menu_input == 4:
            return customer_menu()
        elif main_menu_input == 5:
            return settings_menu()
        else:
            support_functions.clear()
            print(print_statements.error_statement)
            return main()
    except ValueError as err:
            support_functions.clear()
            print(print_statements.error_statement)
            return main()

def product_menu():
    '''Function that calls the product menu of the app.'''
    print(print_statements.product_menu_options)
    try:
        product_menu_input = int(input(print_statements.input_statement))
        if product_menu_input == 0:
            print('Returning to main menu.')
            return main()
        elif product_menu_input == 1:
            sql.retrieve_products_table()
            return product_menu()
        elif product_menu_input == 2:
            sql.insert_into_products()
            return product_menu()
        elif product_menu_input == 3:
            sql.update_product()
            return product_menu()
        elif product_menu_input == 4:
            support_functions.clear()
            sql.retrieve_products_table()
            sql.delete_product()
            return product_menu()
        else:
            print(print_statements.error_statement)
            return product_menu()
    except ValueError as err:
            support_functions.clear()
            print(print_statements.error_statement)
            return product_menu()

def courier_menu():
    '''Function that calls the courier menu of the app.'''
    print(print_statements.courier_menu_options)
    try:
        courier_menu_input = int(input(print_statements.input_statement))
        if courier_menu_input == 0:
            print('Returning to main menu.')
            return main()
        elif courier_menu_input == 1:
            sql.retrieve_couriers_table()
            return courier_menu()
        elif courier_menu_input == 2:
            sql.insert_into_couriers()
            return courier_menu()
        elif courier_menu_input == 3:
            sql.update_courier()
            return courier_menu()
        elif courier_menu_input == 4:
            sql.delete_courier()
            return courier_menu()
        else:
            print(print_statements.error_statement)
            return courier_menu()
    except ValueError as err:
            support_functions.clear()
            print(print_statements.error_statement)
            return courier_menu()

def order_menu():
    '''Function that calls the order menu of the app.'''
    print(print_statements.order_menu_options)
    try:
        order_menu_input = int(input(print_statements.input_statement))
        if order_menu_input == 0:
            print('Returning to main menu.')
            return main()
        elif order_menu_input == 1:
            # Retrieve function here
            return order_menu()
        elif order_menu_input == 2:
            sql.insert_into_orders()
            return order_menu()
        elif order_menu_input == 3:
            # Update function here
            return order_menu()
        elif order_menu_input == 4:
            # Delete function here
            return order_menu()
        else:
            print(print_statements.error_statement)
            return order_menu()
    except ValueError as err:
            support_functions.clear()
            print(print_statements.error_statement)
            return order_menu()

def customer_menu():
    '''Function that calls the customer menu of the app.'''
    print(print_statements.customer_menu_options)
    try:
        customer_menu_input = int(input(print_statements.input_statement))
        if customer_menu_input == 0:
            print('Returning to main menu.')
            return main()
        elif customer_menu_input == 1:
            sql.retrieve_customers_table()
            return order_menu()
        elif customer_menu_input == 2:
            sql.insert_into_customers()
            return order_menu()
        elif customer_menu_input == 3:
            sql.update_customer()
            return order_menu()
        elif customer_menu_input == 4:
            sql.delete_customer()
            return order_menu()
        else:
            print(print_statements.error_statement)
            return order_menu()
    except ValueError as err:
            support_functions.clear()
            print(print_statements.error_statement)
            return product_menu()

def settings_menu():
    '''Function that calls the settings menu of the app.'''
    print('This functionality has not yet been implemented. Stay tuned!')
    pass

if __name__ == '__main__':
    main()