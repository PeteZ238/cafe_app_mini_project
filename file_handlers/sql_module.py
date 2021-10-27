import pymysql as mysql
import tabulate
import modules.print_statements as print_statements
import modules.support_functions as support_functions
import datetime

host = 'localhost'
user = 'root'
password = 'password'

def create_test_environment(database):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    foreign_keys_off = '''SET foreign_key_checks = 0;'''
    drop_products = '''DROP TABLE IF EXISTS products;'''
    drop_couriers = '''DROP TABLE IF EXISTS couriers;'''
    drop_customers = '''DROP TABLE IF EXISTS customers;'''
    drop_order_status = '''DROP TABLE IF EXISTS order_status;'''
    drop_orders = '''DROP TABLE IF EXISTS orders;'''
    drop_order_products = '''DROP TABLE IF EXISTS order_products;'''
    foreign_keys_on = '''SET foreign_key_checks = 1;'''
    products = '''CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_price DOUBLE NOT NULL,
    product_stock INT NOT NULL,
    is_deleted BOOL NOT NULL,
    PRIMARY KEY(product_id)
    );'''
    couriers = '''CREATE TABLE couriers (
    courier_id INT NOT NULL AUTO_INCREMENT,
    courier_name VARCHAR(255) NOT NULL,
    courier_phone VARCHAR(255) NOT NULL,
    is_deleted BOOL NOT NULL,
    PRIMARY KEY(courier_id)
    );'''
    customers = '''CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT,   
    customer_name VARCHAR(255) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(255) NOT NULL,
    is_deleted BOOL NOT NULL,
    PRIMARY KEY(customer_id)
    );'''
    order_status = '''CREATE TABLE order_status (
    order_status_id INT NOT NULL AUTO_INCREMENT,
    order_status VARCHAR(255) NOT NULL,
    PRIMARY KEY(order_status_id)
    );'''
    orders = '''CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL, 
    courier_id INT NOT NULL,
    order_status_id INT NOT NULL,
    order_date VARCHAR(255) NOT NULL,
    order_total_cost DOUBLE,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY(courier_id) REFERENCES couriers (courier_id),
    FOREIGN KEY(order_status_id) REFERENCES order_status (order_status_id)
    );'''
    order_products = '''CREATE TABLE order_products (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders (order_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    );'''
    
    insert_products = '''INSERT INTO products (product_name, product_price, product_stock, is_deleted)
    VALUES ('Coke', 1.25, 12, 0), ('Fanta', 0.75, 15, 0), ('Pepsi', 1, 20, 0); '''
    
    insert_couriers = '''INSERT INTO couriers (courier_name, courier_phone, is_deleted)
    VALUES ('Mike', '07459346523', 0), ('Pete', '07459346523', 0), ('Claire', '07459346523', 0);'''
    
    insert_customers = '''INSERT INTO customers (customer_name, customer_address, customer_phone, is_deleted)
    VALUES ('Pete', 'Standard Avenue, Covenrty', '07429246100', 0),
    ('Kevin', 'Oxford Street, London', '07457582365', 0),
    ('Claire', 'Balsall Common, Warwickshire', '07775505500', 0);'''

    insert_order_status = '''INSERT INTO order_status (order_status)
    VALUES ('preparing'), ('out-for-delivery'), ('delivered'), ('cancelled');'''

    insert_into_orders = '''INSERT INTO orders (customer_id, courier_id, order_status_id, order_date, order_total_cost)
    VALUES (1, 3, 1, '26/10/2021', 2.5),
    (2, 1, 2, '26/10/2021', 2),
    (2, 1, 4, '26/10/2021', 2);'''

    insert_into_order_products = '''INSERT INTO order_products (order_id, product_id, quantity)
    VALUES (1, 1, 2),
    (2, 1, 1), 
    (2, 2, 1),
    (3, 3, 2);'''

    cursor.execute(foreign_keys_off)
    cursor.execute(drop_products)
    cursor.execute(drop_couriers)
    cursor.execute(drop_customers)
    cursor.execute(drop_order_status)
    cursor.execute(drop_orders)
    cursor.execute(drop_order_products)
    cursor.execute(foreign_keys_on)
    cursor.execute(products)
    cursor.execute(couriers)
    cursor.execute(customers)
    cursor.execute(order_status)
    cursor.execute(orders)
    cursor.execute(order_products)
    cursor.execute(insert_products)
    cursor.execute(insert_couriers)
    cursor.execute(insert_customers)
    cursor.execute(insert_order_status)
    cursor.execute(insert_into_orders)
    cursor.execute(insert_into_order_products)

    connection.commit()
    cursor.close()
    connection.close()
    print('Test envvironment created!')

def delete_test_environment(database):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    foreign_keys_off = '''SET foreign_key_checks = 0;'''
    products = '''DROP TABLE products;'''
    couriers = '''DROP TABLE couriers;'''
    customers = '''DROP TABLE customers;'''
    orders = '''DROP TABLE orders;'''
    order_products = '''DROP TABLE order_products;'''
    order_status = '''DROP TABLE order_status;'''
    foreign_keys_on = '''SET foreign_key_checks = 1;'''

    cursor.execute(foreign_keys_off)
    cursor.execute(products)
    cursor.execute(couriers)
    cursor.execute(customers)
    cursor.execute(orders)
    cursor.execute(order_products)
    cursor.execute(order_status)
    cursor.execute(foreign_keys_on)
    
    connection.commit()
    cursor.close()
    connection.close()
    print('Test environment deleted!')

def retrieve_products_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT product_id, product_name, product_price, product_stock FROM products
    WHERE is_deleted = 0;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('product_id', 'product_name', 'product_price', 'product_stock')
    support_functions.clear()
    print('Total number of products in the database: ' + str(cursor.rowcount))
    print('\n')
    print(tabulate.tabulate(result, headers = headers))

    return result

def retrieve_couriers_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT courier_id, courier_name, courier_phone FROM couriers
    WHERE is_deleted = 0;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('courier_id', 'courier_name', 'courier_phone')
    support_functions.clear()
    print('Total number of couriers in the database: ' + str(cursor.rowcount))
    print('\n')
    print(tabulate.tabulate(result, headers = headers))

    return result

def retrieve_customers_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT customer_id, customer_name, customer_address, customer_phone FROM customers
    WHERE is_deleted = 0;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('customer_id', 'customer_name', 'customer_addres', 'customer_phone')
    support_functions.clear()
    print('Total number of customers in the database: ' + str(cursor.rowcount))
    print('\n')
    print(tabulate.tabulate(result, headers = headers))

    return result

def retrieve_order_status_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT * FROM order_status
    WHERE order_status_id != 4;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('order_status_id', 'order_status')
    support_functions.clear()
    print(tabulate.tabulate(result, headers = headers))

    return result

def retrieve_orders_table(database: str = 'cafe_app') -> list:
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    try:
        show_cancelled = int(input(print_statements.order_print_options))
        orders_sort = int(input(print_statements.orders_sort_options))

        if orders_sort == 0:
            sort_id = 'orders.order_id ASC'
        elif orders_sort == 1:
            sort_id = 'orders.order_status_id ASC'
        elif orders_sort == 2:
            sort_id = 'orders.courier_id ASC'
        else:
            sort_id = 'orders.order_id ASC'

        # sort_id_dict = {'sort_id': sort_id}

        if show_cancelled == 0:
            orders = '''
            SELECT orders.order_id, customer_name, courier_name, order_status, order_date, order_total_cost, orders.order_status_id, orders.courier_id
            FROM orders
            INNER JOIN customers
            ON orders.customer_id = customers.customer_id
            INNER JOIN couriers
            ON orders.courier_id = couriers.courier_id
            INNER JOIN order_status
            ON orders.order_status_id = order_status.order_status_id
            WHERE order_status.order_status_id != 4
            ORDER BY ''' + sort_id + ';'

            cursor.execute(orders)

            order_tuple = cursor.fetchall()

            products = '''
            SELECT orders.order_id, product_name, quantity
            FROM orders
            INNER JOIN order_products AS op
            ON orders.order_id = op.order_id
            INNER JOIN products
            ON op.product_id = products.product_id
            WHERE orders.order_status_id != 4;'''

            cursor.execute(products)

            product_tuple = cursor.fetchall()
            print(product_tuple)

        elif show_cancelled == 1:
            orders = '''
            SELECT orders.order_id, customer_name, courier_name, order_status, order_date, order_total_cost, orders.order_status_id, orders.courier_id
            FROM orders
            INNER JOIN customers
            ON orders.customer_id = customers.customer_id
            INNER JOIN couriers
            ON orders.courier_id = couriers.courier_id
            INNER JOIN order_status
            ON orders.order_status_id = order_status.order_status_id
            ORDER BY ''' + sort_id + ';'

            cursor.execute(orders)
            # print(cursor._last_executed)

            order_tuple = cursor.fetchall()

            products = '''
            SELECT orders.order_id, product_name, quantity
            FROM orders
            INNER JOIN order_products AS op
            ON orders.order_id = op.order_id
            INNER JOIN products
            ON op.product_id = products.product_id;'''

            cursor.execute(products)

            product_tuple = cursor.fetchall()

        else:
            orders = '''
            SELECT orders.order_id, customer_name, courier_name, order_status, order_date, order_total_cost, orders.order_status_id, orders.courier_id
            FROM orders
            INNER JOIN customers
            ON orders.customer_id = customers.customer_id
            INNER JOIN couriers
            ON orders.courier_id = couriers.courier_id
            INNER JOIN order_status
            ON orders.order_status_id = order_status.order_status_id
            WHERE order_status.order_status_id != 4
            ORDER BY ''' + sort_id + ';'

            cursor.execute(orders)

            order_tuple = cursor.fetchall()

            products = '''
            SELECT orders.order_id, product_name, quantity
            FROM orders
            INNER JOIN order_products AS op
            ON orders.order_id = op.order_id
            INNER JOIN products
            ON op.product_id = products.product_id
            WHERE orders.order_status_id != 4;'''

            cursor.execute(products)

            product_tuple = cursor.fetchall()

    except ValueError as err:
        print(err)
        return ValueError

    order_list = []

    for count, value in enumerate(order_tuple):
        order_dict = {}
        order_id = order_tuple[count][0]
        order_dict['order_id'] = order_id
        order_dict['customer_name'] = order_tuple[count][1]
        order_dict['courier_name'] = order_tuple[count][2]
        order_dict['order_status'] = order_tuple[count][3]
        product_list = []
        for c, v in enumerate(product_tuple):
            if order_id == product_tuple[c][0]:
                product_dict = {}
                product_dict['product'] = product_tuple[c][1]
                product_dict['quantity'] = product_tuple[c][2]
                product_list.append(product_dict)
                order_dict['product_list'] = product_list
        order_dict['date'] = order_tuple[count][4]
        order_dict['order_total_cost'] = order_tuple[count][5]
        order_list.append(order_dict)

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = 'keys'
    support_functions.clear()
    print(tabulate.tabulate(order_list, headers = headers))
    return order_list

def insert_into_products(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''INSERT INTO products (product_name, product_price, product_stock, is_deleted)
    VALUES (%(product_name)s, %(product_price)s, %(product_stock)s, %(is_deleted)s);'''

    support_functions.clear()
    retrieve_products_table()

    try:
        product_name = input('\n' + 'What is the name of the product you would like to add? ')
        product_price = float(input('\n' + 'What is the price of the product you would like to add? '))
        product_stock = int(input('\n' + 'How many of this product are in stock? '))

        product_dict = {'product_name': product_name, 'product_price': product_price, 'product_stock': product_stock, 'is_deleted': 0}

        cursor.execute(sql, product_dict)
    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def insert_into_couriers(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''INSERT INTO couriers (courier_name, courier_phone, is_deleted)
    VALUES (%(courier_name)s, %(courier_phone)s, %(is_deleted)s);'''

    support_functions.clear()
    retrieve_couriers_table()

    courier_name = input('\n' + 'What is the name of the courier you would like to add? ')
    courier_phone = input('\n' + 'What is the phone number of the courier you would like to add? ')

    courier_dict = {'courier_name': courier_name, 'courier_phone': courier_phone, 'is_deleted': 0}

    cursor.execute(sql, courier_dict)

    connection.commit()
    cursor.close()
    connection.close()

def insert_into_customers(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''INSERT INTO customers (customer_name, customer_address, customer_phone, is_deleted)
    VALUES (%(customer_name)s, %(customer_address)s, %(customer_phone)s, %(is_deleted)s);'''

    support_functions.clear()
    retrieve_customers_table()

    customer_name = input('\n' + 'What is the name of the customer? ')
    customer_address = input('\n' + 'What is the customer\'s address? ')
    customer_phone = input('\n' + 'What is the customer\'s phone number? ')

    customer_dict = {'customer_name': customer_name, 'customer_address': customer_address, 'customer_phone': customer_phone, 'is_deleted': 0}

    cursor.execute(sql, customer_dict)

    connection.commit()
    cursor.close()
    connection.close()

def get_product(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    try:
        support_functions.clear()
        retrieve_products_table(database)
        product_selection = int(input('\n' + 'Please select the id of the product you would like to add to the order: '))
        
        get_product_ids = '''SELECT product_id FROM products
        WHERE EXISTS(SELECT * FROM products WHERE product_id = %(product_id)s)'''
        product_id_dict = {'product_id': product_selection}
        cursor.execute(get_product_ids, product_id_dict)
        customer_rowcount = cursor.rowcount

        if customer_rowcount == 0:
            print('Invalid product selection.')
            connection.commit()
            cursor.close()
            connection.close()
            return 'Invalid product_id selection.'

        sql = '''SELECT * FROM products WHERE product_id = %(product_selection)s;'''

        selection_dict = {'product_selection': product_selection}

        cursor.execute(sql, selection_dict)
        selection_tuple = cursor.fetchall()

        product_id = selection_tuple[0][0]
        product_name = selection_tuple[0][1]
        product_stock = selection_tuple[0][3]

        quantity_selection = int(input('\n' + 'How many of this product would you like to add to the order? '))

        if quantity_selection <= product_stock:

            stock = '''UPDATE products
            SET product_stock = %(updated_product_stock)s
            WHERE product_id = %(product_id)s'''

            updated_product_stock = product_stock - quantity_selection
            stock_dict = {'updated_product_stock': updated_product_stock, 'product_id': product_id}

            cursor.execute(stock, stock_dict)

            connection.commit()
            cursor.close()
            connection.close()

            return (product_id, quantity_selection)
        elif quantity_selection > product_stock:
            print(f'There is not enough {product_name}\'s in stock to fullfil this order.')
            return 'Insufficient stock error'
    except ValueError as err:
        print(err)
        return ValueError

def get_total_cost(order_id, database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''SELECT p.product_price, op.quantity
    FROM order_products op
    INNER JOIN products p
    ON op.product_id = p.product_id
    WHERE op.order_id = %(order_id)s;'''

    sql_dict = {'order_id': order_id}

    cursor.execute(sql, sql_dict)
    price_tuple = cursor.fetchall()

    order_total_cost = 0

    for count, value in enumerate(price_tuple):
        price = price_tuple[count][0]
        quantity = price_tuple[count][1]
        total = price * quantity
        order_total_cost += total

    cost = '''UPDATE orders 
    SET order_total_cost = %(order_total_cost)s
    WHERE order_id = %(order_id)s;'''
    cost_dict = {'order_total_cost': order_total_cost, 'order_id': order_id}
    cursor.execute(cost, cost_dict)

    connection.commit()
    cursor.close()
    connection.close()

    return order_total_cost

def insert_products_into_order(order_id, database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)
    cursor = connection.cursor()

    try:
        product_list = []
        indicator = 0
        while indicator == 0:
            product_tuple = get_product(database)
            if  product_tuple == 'Invalid product_id selection.':
                sql = '''UPDATE orders SET order_status_id = 4 WHERE order_id = %(order_id)s;'''
                order_id_dict = {'order_id' :order_id}
                cursor.execute(sql, order_id_dict)
                connection.commit()
                return'Invalid product_id selection.'
            elif product_tuple == 'Insufficient stock error':
                sql = '''UPDATE orders SET order_status_id = 4 WHERE order_id = %(order_id)s;'''
                order_id_dict = {'order_id' :order_id}
                cursor.execute(sql, order_id_dict)
                connection.commit()
                return 'Insufficient stock error'
            elif product_tuple == ValueError:
                sql = '''UPDATE orders SET order_status_id = 4 WHERE order_id = %(order_id)s;'''
                order_id_dict = {'order_id' :order_id}
                cursor.execute(sql, order_id_dict)
                connection.commit()
                return ValueError
            else:
                product_list.append(product_tuple)
            add_another_product = input('\n' + 'Would you like to add another product to the order? [Y/N] ')
            if add_another_product[0].lower() == 'y':
                continue
            else:
                indicator = 1

        product_dicts = []
        for i in range(len(product_list)):
            product_dict = {}
            product_dict['order_id'] = order_id
            product_dict['product_id'] = product_list[i][0]
            product_dict['quantity'] = product_list[i][1]
            product_dicts.append(product_dict)

        order_products = '''INSERT INTO order_products (order_id, product_id, quantity)
        VALUES (%(order_id)s, %(product_id)s, %(quantity)s)'''

        cursor.executemany(order_products, product_dicts)

        connection.commit()

        cursor.close()
        connection.close()

    except ValueError as err:
        print(err)
        return ValueError

def insert_into_orders(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    try:
        cursor = connection.cursor()
        support_functions.clear()
        retrieve_customers_table(database)
        customer_id = int(input(print_statements.customer_selection))

        get_customer_ids = '''SELECT customer_id FROM customers
        WHERE EXISTS(SELECT * FROM customers WHERE customer_id = %(customer_id)s)'''
        customer_id_dict = {'customer_id': customer_id}
        cursor.execute(get_customer_ids, customer_id_dict)
        customer_rowcount = cursor.rowcount

        if customer_rowcount == 0:
            print('Invalid customer selection.')
            connection.commit()
            cursor.close()
            connection.close()
            return 'Invalid customer selection.'

        support_functions.clear()
        retrieve_couriers_table(database)
        courier_id = int(input(print_statements.courier_selection))

        get_courier_ids = '''SELECT courier_id FROM couriers
        WHERE EXISTS(SELECT * FROM couriers WHERE courier_id = %(courier_id)s)'''
        courier_id_dict = {'courier_id': courier_id}
        cursor.execute(get_courier_ids, courier_id_dict)
        courier_rowcount = cursor.rowcount

        if courier_rowcount == 0:
            print('Invalid courier selection.')
            connection.commit()
            cursor.close()
            connection.close()
            return 'Invalid courier selection.'
        
        order = '''INSERT INTO orders (customer_id, courier_id, order_status_id, order_date)
        VALUES (%(customer_id)s, %(courier_id)s, %(order_status_id)s, %(order_date)s);'''

        date = datetime.datetime.now()
        day = date.day
        month = date.month
        year = date.year
        date_str = f'{day}/{month}/{year}'

        order_dict = {'customer_id': customer_id, 'courier_id': courier_id, 'order_status_id': 1, 'order_date': date_str}

        cursor.execute(order, order_dict)
        connection.commit()
        order_id = cursor.lastrowid

        products = insert_products_into_order(order_id, database)

        get_total_cost(order_id, database)

        connection.commit()
        cursor.close()
        connection.close()
        return products
    
    except ValueError as err:
        print(err)
        return ValueError

def update_product(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    support_functions.clear()
    retrieve_products_table()
    
    try:
        select_product = int(input(print_statements.update_selection))
        print('\n')
        update_selection = int(input(print_statements.product_update_options))

        if update_selection == 0:
            name_update = input('\n' + 'What would you like to update the product name to? ')

            sql = '''UPDATE products
            SET product_name = %(name_update)s
            WHERE product_id = %(select_product)s;'''

            name_update_dict = {'name_update': name_update, 'select_product': select_product}

            cursor.execute(sql, name_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        elif update_selection == 1:
            price_update = float(input('\n' + 'What would you like to update the product price to? '))

            sql = '''UPDATE products
            SET product_price = %(price_update)s
            WHERE product_id = %(select_product)s;'''

            price_update_dict = {'price_update': price_update, 'select_product': select_product}

            cursor.execute(sql, price_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        elif update_selection == 2:
            stock_update = int(input('\n' + 'What would you like to update the product stock to? '))

            sql = '''UPDATE products
            SET product_stock = %(stock_update)s
            WHERE product_id = %(select_product)s;'''

            stock_update_dict = {'stock_update': stock_update, 'select_product': select_product}

            cursor.execute(sql, stock_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        else:
            print(print_statements.error_statement)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def update_courier(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    support_functions.clear()
    retrieve_couriers_table()    
    
    try:
        select_courier = int(input(print_statements.update_selection))
        print('\n')
        update_selection = int(input(print_statements.courier_update_options))

        if update_selection == 0:
            name_update = input('\n' + 'What would you like to update the courier name to? ')

            sql = '''UPDATE couriers
            SET courier_name = %(name_update)s
            WHERE courier_id = %(select_courier)s;'''

            name_update_dict = {'name_update': name_update, 'select_courier': select_courier}

            cursor.execute(sql, name_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        elif update_selection == 1:
            price_update = input('\n' + 'What would you like to update the courier phone to? ')

            sql = '''UPDATE couriers
            SET courier_phone = %(price_update)s
            WHERE courier_id = %(select_courier)s;'''

            courier_update_dict = {'price_update': price_update, 'select_courier': select_courier}

            cursor.execute(sql, courier_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        else:
            print(print_statements.error_statement)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def update_customer(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    support_functions.clear()
    retrieve_customers_table()
    
    try:
        select_customer = int(input(print_statements.update_selection))
        print('\n')
        update_selection = int(input(print_statements.customer_update_options))

        if update_selection == 0:
            name_update = input('\n' + 'What would you like to update the customer name to? ')

            sql = '''UPDATE customers
            SET customer_name = %(name_update)s
            WHERE customer_id = %(select_customer)s;'''

            name_update_dict = {'name_update': name_update, 'select_customer': select_customer}

            cursor.execute(sql, name_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)

        elif update_selection == 1:
            address_update = input('\n' + 'What would you like to update the customer address to? ')

            sql = '''UPDATE customers
            SET customer_address = %(address_update)s
            WHERE customer_id = %(select_customer)s;'''

            address_update_dict = {'address_update': address_update, 'select_customer': select_customer}

            cursor.execute(sql, address_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        elif update_selection == 2:
            phone_update = input('\n' + 'What would you like to update the customer phone number to? ')

            sql = '''UPDATE customers
            SET customer_phone = %(phone_update)s
            WHERE customer_id = %(select_customer)s;'''

            phone_update_dict = {'phone_update': phone_update, 'select_customer': select_customer}

            cursor.execute(sql, phone_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        else:
            print(print_statements.error_statement)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def update_order(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    support_functions.clear()
    retrieve_orders_table()
    
    try:
        select_order = int(input(print_statements.update_selection))
        print('\n')
        update_selection = int(input(print_statements.order_update_options))

        if update_selection == 0:
            print('\n')
            retrieve_customers_table(database)
            customer_id = int(input('\n' + 'Please select the id that you would like to update the customer to: '))

            sql = '''UPDATE orders
            SET customer_id = %(customer_id)s
            WHERE order_id = %(select_order)s;'''

            customer_update_dict = {'customer_id': customer_id, 'select_order': select_order}

            cursor.execute(sql, customer_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)

        elif update_selection == 1:
            restock(select_order, database)

            delete_products = '''DELETE FROM order_products
            WHERE order_id = %(select_order)s;'''

            delete_products_dict = {'select_order': select_order}

            cursor.execute(delete_products, delete_products_dict)
            connection.commit()

            insert_products_into_order(select_order, database)

            get_total_cost(select_order, database)

        elif update_selection == 2:
            retrieve_couriers_table(database)
            courier_id = int(input('\n' + 'Please select the id that you would like to update the courier to: '))

            sql = '''UPDATE orders
            SET courier_id = %(courier_id)s
            WHERE order_id = %(select_order)s;'''

            courier_update_dict = {'courier_id': courier_id, 'select_order': select_order}

            cursor.execute(sql, courier_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)

        elif update_selection == 3:
            retrieve_order_status_table(database)
            order_status_id = int(input('\n' + 'Please select the id that you would like to update the order status to: '))

            sql = '''UPDATE orders
            SET order_status_id = %(order_status_id)s
            WHERE order_id = %(select_order)s;'''

            phone_update_dict = {'order_status_id': order_status_id, 'select_order': select_order}

            cursor.execute(sql, phone_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)

        else:
            print(print_statements.error_statement)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def delete_product(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''UPDATE products
    SET is_deleted = 1
    WHERE product_id = %(product_id)s;'''
    try:
        support_functions.clear()
        retrieve_products_table(database)
        print('\n')
        select_id = int(input(print_statements.deletion_selection))

        selection_dict = {'product_id': select_id}

        cursor.execute(sql, selection_dict)
        print_record_num = cursor.rowcount, 'records deleted.'
        print(print_record_num)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def delete_courier(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''UPDATE couriers
    SET is_deleted = 1
    WHERE courier_id = %(courier_id)s;'''
    try:
        support_functions.clear()
        retrieve_products_table(database)
        print('\n')
        select_id = int(input(print_statements.deletion_selection))

        selection_dict = {'courier_id': select_id}

        cursor.execute(sql, selection_dict)
        print_record_num = cursor.rowcount, 'records deleted.'
        print(print_record_num)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def delete_customer(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''UPDATE customers
    SET is_deleted = 1
    WHERE customer_id = %(customer_id)s;'''
    try:
        support_functions.clear()
        retrieve_products_table(database)
        print('\n')
        select_id = int(input(print_statements.deletion_selection))

        selection_dict = {'customer_id': select_id}

        cursor.execute(sql, selection_dict)
        print_record_num = cursor.rowcount, 'records deleted.'
        print(print_record_num)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def cancel_order(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''UPDATE orders
    SET order_status_id = 4
    WHERE order_id = %(order_id)s;'''
    try:
        support_functions.clear()
        retrieve_products_table(database)
        print('\n')
        select_id = int(input(print_statements.deletion_selection))

        selection_dict = {'order_id': select_id}

        cursor.execute(sql, selection_dict)
        print_record_num = cursor.rowcount, 'records deleted.'
        print(print_record_num)

        restock(select_id, database)

    except ValueError as err:
        print(err)
        return ValueError

    connection.commit()
    cursor.close()
    connection.close()

def restock(order_id, database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    products = '''
    SELECT orders.order_id, op.product_id, op.quantity
    FROM orders
    INNER JOIN order_products AS op
    ON orders.order_id = op.order_id
    INNER JOIN products
    ON op.product_id = products.product_id
    WHERE orders.order_id = %(order_id)s;'''

    order_id_dict = {'order_id': order_id}

    cursor.execute(products, order_id_dict)

    product_tuple = cursor.fetchall()

    for count, value in enumerate(product_tuple):
        product_id = product_tuple[count][1]
        quantity = product_tuple[count][2]

        stock_update = '''
        UPDATE products
        SET product_stock = product_stock + %(quantity)s
        WHERE product_id = %(product_id)s'''

        stock_update_dict = {'quantity': quantity, 'product_id': product_id}

        cursor.execute(stock_update, stock_update_dict)

    connection.commit()
    cursor.close()
    connection.close()