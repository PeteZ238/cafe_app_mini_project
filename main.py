import modules.print_statements as print_statements
import modules.support_functions as support_functions
import modules.record_classes as records
import file_handlers.csv_module as csv

products = csv.products_init()
couriers = csv.couriers_init()
customers = csv.customers_init()
orders = csv.orders_init()

def main():
    '''Method that calls the main menu of the app.'''
    support_functions.clear()
    print(print_statements.main_menu_options)
    main_menu_input = int(input(print_statements.input_statement))
    if main_menu_input == 0:
        support_functions.clear()
        csv.products_update(products)
        csv.couriers_update(couriers)
        csv.orders_update(orders)
        csv.customers_update(customers)
        print(print_statements.exit_statement)
        quit()
    elif main_menu_input == 1:
        support_functions.clear()
        product_menu()
    elif main_menu_input == 2:
        support_functions.clear()
        courier_menu()
    elif main_menu_input == 3:
        support_functions.clear()
        order_menu()
    elif main_menu_input == 4:
        customer_menu()
    elif main_menu_input == 5:
        settings_menu()
    else:
        support_functions.clear()
        print(print_statements.error_statement)
        main()

def product_menu():
    '''Function that calls the product menu of the app.'''
    print(print_statements.product_menu_options)
    product_menu_input = int(input(print_statements.input_statement))
    if product_menu_input == 0:
        print('Returning to main menu.')
        main()
    elif product_menu_input == 1:
        support_functions.list_repr(products)
        product_menu()
    elif product_menu_input == 2:
        temp_object = records.Product()
        temp_dict = temp_object.generate_dict()
        products.append(temp_dict)
        csv.products_update(products)
        product_menu()
    elif product_menu_input == 3:
        support_functions.update_product(products)
        csv.products_update(products)
        product_menu()
    elif product_menu_input == 4:
        support_functions.delete_record(products)
        csv.products_update(products)
        product_menu()
    else:
        print(print_statements.error_statement)
        product_menu()

def courier_menu():
    '''Function that calls the courier menu of the app.'''
    print(print_statements.courier_menu_options)
    courier_menu_input = int(input(print_statements.input_statement))
    if courier_menu_input == 0:
        print('Returning to main menu.')
        main()
    elif courier_menu_input == 1:
        support_functions.list_repr(couriers)
        courier_menu()
    elif courier_menu_input == 2:
        temp_object = records.Courier()
        temp_dict = temp_object.generate_dict()
        couriers.append(temp_dict)
        csv.couriers_update(couriers)
        courier_menu()
    elif courier_menu_input == 3:
        support_functions.update_courier(couriers)
        csv.couriers_update(couriers)
        courier_menu()
    elif courier_menu_input == 4:
        support_functions.delete_record(couriers)
        csv.couriers_update(couriers)
        courier_menu()
    else:
        print(print_statements.error_statement)
        courier_menu()

def order_menu():
    '''Function that calls the order menu of the app.'''
    print(print_statements.order_menu_options)
    order_menu_input = int(input(print_statements.input_statement))
    if order_menu_input == 0:
        print('Returning to main menu.')
        main()
    elif order_menu_input == 1:
        support_functions.list_repr(orders)
        order_menu()
    elif order_menu_input == 2:
        temp_object = records.Order()
        temp_dict = temp_object.generate_dict()
        orders.append(temp_dict)
        csv.orders_update(orders)
        order_menu()
    elif order_menu_input == 3:
        support_functions.update_order(orders, customers, products, couriers)
        csv.orders_update(orders)
        order_menu()
    elif order_menu_input == 4:
        support_functions.delete_record(orders)
        csv.orders_update(orders)
        order_menu()
    else:
        print(print_statements.error_statement)
        order_menu()

def customer_menu():
    '''Function that calls the customer menu of the app.'''
    print(print_statements.customer_menu_options)
    customer_menu_input = int(input(print_statements.input_statement))
    if customer_menu_input == 0:
        print('Returning to main menu.')
        main()
    elif customer_menu_input == 1:
        support_functions.list_repr(customers)
        order_menu()
    elif customer_menu_input == 2:
        temp_object = records.Customer()
        temp_dict = temp_object.generate_dict()
        customers.append(temp_dict)
        csv.customers_update(customers)
        order_menu()
    elif customer_menu_input == 3:
        support_functions.update_customer(customers)
        csv.customers_update(customers)
        order_menu()
    elif customer_menu_input == 4:
        support_functions.delete_record(customers)
        csv.customers_update(customers)
        order_menu()
    else:
        print(print_statements.error_statement)
        order_menu()

def settings_menu():
    '''Function that calls the settings menu of the app.'''
    pass

if __name__ == '__main__':
    main()