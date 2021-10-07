import subprocess
import platform
import modules.print_statements as print_statements

def clear():
    '''Function that clears the terminal screen.'''
    if platform.system() == 'Windows':
        subprocess.run('cls', shell = True)
    else:
        subprocess.run('clear', shell = True)

def get_customer_details():
    customer_name = input('What is the name of the customer? ')
    customer_address = input('What is the customer address? ')
    customer_phone = input('What is the customer\'s phone number? ')
    return customer_name, customer_address, customer_phone

def get_product_order(products):
    print('\n')
    print('The available products are:')
    print(products)
    order = []
    order_switch = 0
    while order_switch == 0:
        product_order_input = input('What product would you like to add to the order? ')
        if product_order_input in products:
            order.append(product_order_input)
            repeat_action = input('Product added to order. Would you like to add another product to the order? [Y/N] ').lower()
            if repeat_action[0] == 'y':
                order_switch = 0
            else:
                order_switch = 1
        else:
            print('Product is not in the menu. Please add a valid product off the menu.')
    return order

def get_courier_details(couriers):
    print('\n')
    print('The available couriers are:')
    print(couriers)
    courier_assigned = input('What is the name of the courier for this order? ')
    while courier_assigned not in couriers:
        print('Courier does not exist. Please add a valid courier name.')
        courier_assigned = input('What is the name of the courier for this order? ')
    return courier_assigned

def get_order_status():
    order_status_input = int(input(print_statements.order_status_options))
    if order_status_input == 0:
        order_status = 'preparing'
    elif order_status_input == 1:
        order_status = 'out-for-delivery'
    elif order_status_input == 2:
        order_status = 'delivered'
    else:
        print('Order status invalid. Please select order status.')
        get_order_status()
    return order_status

def order_dict(customer_name, customer_address, customer_phone, product_order, courier_details, order_status):
    order_dict = {}
    order_dict['customer_name'] = customer_name
    order_dict['customer_address'] = customer_address
    order_dict['customer_phone'] = customer_phone
    order_dict['product_order'] = product_order
    order_dict['courier'] = courier_details
    order_dict['status'] = order_status
    return order_dict 