import csv
from pathlib import Path

def orders_init(orders_filename = 'data\orders.csv'):
    '''Function that initialises the orders csv file.'''
    if Path(orders_filename).exists() == False:
        with open(orders_filename, 'w+', newline = '') as order_file:
            field_names = ['id', 'customer_name', 'customer_address', 'customer_phone', 'product_order', 'courier', 'status']
            order_writer = csv.DictWriter(order_file, fieldnames = field_names)
        order_file.close()
    
    with open(orders_filename, 'r+', newline = '') as order_file:
        order_reader = csv.DictReader(order_file)
        list_from_csv = list(order_reader)
        orders = []
        for i in range(len(list_from_csv)):
            orders.append(dict(list_from_csv[i]))
    order_file.close()    
    return orders

def orders_update(orders, orders_filename = 'data\orders.csv'):
    '''Function that updates the orders csv file.'''
    for i in range(len(orders)):
        orders[i]['id'] = i
    with open(orders_filename, 'w+', newline = '') as order_file:
        field_names = ['id', 'customer_name', 'customer_address', 'customer_phone', 'product_order', 'courier', 'status']
        order_writer = csv.DictWriter(order_file, fieldnames = field_names)
        order_writer.writeheader()
        for item in orders:
            order_writer.writerow(item) 
    order_file.close()

def products_init(products_filename = 'data\products.csv'):
    '''Function that initialises the products csv file.'''
    if Path(products_filename).exists() == False:
        with open(products_filename, 'w', newline = '') as product_file:
            field_names = ['id','product_name', 'product_price']
            products_writer = csv.DictWriter(product_file, fieldnames = field_names)
        product_file.close()
    
    with open(products_filename, 'r+', newline = '') as product_file:
        product_reader = csv.DictReader(product_file)
        list_from_csv = list(product_reader)
        products = []
        for i in range(len(list_from_csv)):
            products.append(dict(list_from_csv[i]))
    product_file.close()    
    return products

def products_update(products, products_filename = 'data\products.csv'):
    '''Function that updates the products csv file.'''
    for i in range(len(products)):
        products[i]['id'] = i
    with open(products_filename, 'w', newline = '') as product_file:
        fieldnames = ['id','product_name', 'product_price']
        product_writer = csv.DictWriter(product_file, fieldnames = fieldnames)
        product_writer.writeheader()
        for item in products:
            product_writer.writerow(item) 
    product_file.close()

def couriers_init(couriers_filename = 'data\couriers.csv'):
    '''Function that initialises the couriers csv file.'''
    if Path(couriers_filename).exists() == False:
        with open(couriers_filename, 'w+', newline = '') as courier_file:
            field_names = ['id', 'courier_name', 'courier_phone']
            courier_writer = csv.DictWriter(courier_file, fieldnames = field_names)
        courier_file.close()
    
    with open(couriers_filename, 'r+', newline = '') as courier_file:
        courier_reader = csv.DictReader(courier_file)
        list_from_csv = list(courier_reader)
        couriers = []
        for i in range(len(list_from_csv)):
            couriers.append(dict(list_from_csv[i]))
    courier_file.close()    
    return couriers

def couriers_update(couriers, couriers_filename = 'data\couriers.csv'):
    '''Function that updates the couriers csv file.'''
    for i in range(len(couriers)):
        couriers[i]['id'] = i
    with open(couriers_filename, 'w+', newline = '') as courier_file:
        field_names = ['id','courier_name', 'courier_phone']
        courier_writer = csv.DictWriter(courier_file, fieldnames = field_names)
        courier_writer.writeheader()
        for item in couriers:
            courier_writer.writerow(item) 
    courier_file.close()

def customers_init(customers_filename = 'data\customers.csv'):
    '''Function that initialises the customers csv file.'''
    if Path(customers_filename).exists() == False:
        with open(customers_filename, 'w+', newline = '') as customer_file:
            field_names = ['id', 'customer_name', 'customer_address', 'customer_phone']
            customer_writer = csv.DictWriter(customer_file, fieldnames = field_names)
        customer_file.close()
    
    with open(customers_filename, 'r+', newline = '') as customer_file:
        customer_reader = csv.DictReader(customer_file)
        list_from_csv = list(customer_reader)
        customers = []
        for i in range(len(list_from_csv)):
            customers.append(dict(list_from_csv[i]))
    customer_file.close()    
    return customers

def customers_update(customers, customers_filename = 'data\customers.csv'):
    '''Function that updates the customers csv file.'''
    for i in range(len(customers)):
        customers[i]['id'] = i
    with open(customers_filename, 'w+', newline = '') as customer_file:
        field_names = ['id', 'customer_name', 'customer_address', 'customer_phone']
        customer_writer = csv.DictWriter(customer_file, fieldnames = field_names)
        customer_writer.writeheader()
        for item in customers:
            customer_writer.writerow(item) 
    customer_file.close()