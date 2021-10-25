import modules.print_statements as print_statements
import modules.support_functions as support_functions
import tabulate
import subprocess
import platform

def clear():
    '''Function that clears the terminal screen.'''
    if platform.system() == 'Windows':
        subprocess.run('cls', shell = True)
    else:
        subprocess.run('clear', shell = True)

def list_repr(input_list: list):
    '''Function that prints and formats lists to improve readability.'''
    clear()
    if len(input_list) == 0:
        print(input_list)
    else:
        print(tabulate.tabulate(input_list, headers = 'keys'))

def delete_record(record: list):
    '''Function that deletes a record based on user input.'''
    user_input = int(input(print_statements.deletion_selection))
    if user_input <= (len(record) - 1):
        record.pop(user_input)
        return record
    else:
        print(print_statements.error_statement)

def update_product(product_list: list) -> list:
    clear()
    list_repr(product_list)
    select_product = int(input(print_statements.update_selection))
    if select_product <= (len(product_list) - 1):
        product_update = [{0: 'Product Name', 1: 'Product Price'}]
        clear()
        list_repr(product_update)
        update_selection = int(input(print_statements.update_selection))
        if update_selection == 0:
            name_update = input('What would you like to update the product name to? ')
            product_list[select_product]['product_name'] = name_update
            return product_list
        elif update_selection == 1:
            price_update = input('What would you like to update the product price to? ')
            product_list[select_product]['product_price'] = price_update
            return product_list
        else:
            print(print_statements.error_statement)
    else:
        print(print_statements.error_statement)

def update_courier(courier_list: list) -> list:
    clear()
    list_repr(courier_list)
    select_courier = int(input(print_statements.update_selection))
    if select_courier <= (len(courier_list) - 1):
        courier_update = [{0: 'Courier Name', 1 :'Courier Phone Number'}]
        clear()
        list_repr(courier_update)
        update_selection = int(input(print_statements.update_selection))
        if update_selection == 0:
            name_update = input('What would you like to update the courier name to? ')
            courier_list[select_courier]['courier_name'] = name_update
            return courier_list
        elif update_selection == 1:
            phone_update = input('What would you like to update the phone number to? ')
            courier_list[select_courier]['courier_phone'] = phone_update
            return courier_list
        else:
            print(print_statements.error_statement)
    else:
        print(print_statements.error_statement)

def update_customer(customer_list: list) -> list:
    clear()
    list_repr(customer_list)
    select_customer = int(input(print_statements.update_selection))
    if select_customer <= (len(customer_list) - 1):
        customer_update = [{0: 'Customer Name', 1 :'Customer Address', 2: 'Customer Phone Number'}]
        clear()
        list_repr(customer_update)
        update_selection = int(input(print_statements.update_selection))
        if update_selection == 0:
            name_update = input('What would you like to update the customer name to? ')
            customer_list[select_customer]['customer_name'] = name_update
            return customer_list
        elif update_selection == 1:
            address_update = input('What would you like to update the customer address to? ')
            customer_list[select_customer]['customer_address'] = address_update
            return customer_list
        elif update_selection == 2:
            phone_update = input('What would you like to update the customer phone number to? ')
            customer_list[select_customer]['customer_phone'] = phone_update
            return customer_list
        else:
            print(print_statements.error_statement)
    else:
        print(print_statements.error_statement)

def update_order(order_list: list, customer_list: list, product_list: list, courier_list: list) -> list:
    clear()
    list_repr(order_list)
    select_order = int(input(print_statements.update_selection))
    if select_order <= (len(order_list) - 1):
        order_update = [{0: 'Customer', 1 :'Product Order', 2: 'Courier', 3: 'Order Status'}]
        clear()
        list_repr(order_update)
        update_selection = int(input(print_statements.update_selection))
        if update_selection == 0:
            get_customer(order_list[update_selection], customer_list)
            return order_list
        elif update_selection == 1:
            get_products(order_list[update_selection], product_list)
            return order_list
        elif update_selection == 2:
            get_courier(order_list[update_selection], courier_list)
            return order_list
        elif update_selection == 3:
            get_order_status(order_list[update_selection])
            return order_list
        else:
            print(print_statements.error_statement)
    else:
        print(print_statements.error_statement)

def get_customer(order: dict, customer_list: list) -> dict:
    clear()
    list_repr(customer_list)
    select_customer = int(input(print_statements.customer_selection))
    cust_dict = customer_list[select_customer]
    order['customer_name'] = cust_dict['customer_name']
    order['customer_address'] = cust_dict['customer_address']
    order['customer_phone'] = cust_dict['customer_phone']
    return order

def get_courier(order: dict, courier_list: list) -> dict:
    clear()
    list_repr(courier_list)
    select_courier = int(input(print_statements.courier_selection))
    courier_dict = courier_list[select_courier]
    order['courier_name'] = courier_dict['courier_name']
    order['courier_phone'] = courier_dict['courier_phone']
    return order

def get_products(order: dict, product_list: list) -> dict:
    clear()
    list_repr(product_list)
    product_order = []
    select_products = input(print_statements.product_selection)
    select_products.split(',')
    for ind in select_products:
        product_order.append(product_list[int(ind)])
    order['product_order'] = product_order
    return order

def get_order_status(order: dict):
    order_status = ['preparing', 'out-for-delivery', 'delivered']
    clear()
    for i in range(len(order_status)):
        print(f'{i}: {order_status[i]} \n')
    select_order_status = int(input(print_statements.order_status_selection))
    order['order_status'] = order_status[select_order_status]
    return order