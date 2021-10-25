import pymysql as mysql
import tabulate
import modules.print_statements as print_statements
import modules.support_functions as support_functions

host = 'localhost'
user = 'root'
password = 'password'

def create_test_environment(database):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    products = '''CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_price DOUBLE NOT NULL,
    product_stock INT NOT NULL,
    PRIMARY KEY(product_id)
    );'''
    couriers = '''CREATE TABLE couriers (
    courier_id INT NOT NULL AUTO_INCREMENT,
    courier_name VARCHAR(255) NOT NULL,
    courier_phone VARCHAR(255) NOT NULL,
    PRIMARY KEY(courier_id)
    );'''
    customers = '''CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT,   
    customer_name VARCHAR(255) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(255) NOT NULL,
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
    
    insert_products = '''INSERT INTO products (product_name, product_price, product_stock)
    VALUES ('Coke', 1.25, 12), ('Fanta', 0.75, 15), ('Pepsi', 1, 20);'''
    
    insert_couriers = '''INSERT INTO couriers (courier_name, courier_phone)
    VALUES ('Mike', '07459346523'), ('Pete', '07459346523'), ('Claire', '07459346523');'''
    
    insert_customers = '''INSERT INTO customers (customer_name, customer_address, customer_phone)
    VALUES ('Pete', 'Standard Avenue, Covenrty', '07429246100'),
    ('Kevin', 'Oxford Street, London', '07457582365'),
    ('Claire', 'Balsall Common, Warwickshire', '07775505500');'''

    insert_order_status = '''INSERT INTO order_status (order_status)
    VALUES ('preparing'), ('out-for-delivery'), ('delivered');'''

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
    print('Test envvironment deleted!')

def retrieve_products_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT * FROM products;'''

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
    SELECT * FROM couriers;'''

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
    SELECT * FROM customers;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('customer_id', 'customer_name', 'customer_addres', 'customer_phone')
    support_functions.clear()
    print('Total number of couriers in the database: ' + str(cursor.rowcount))
    print('\n')
    print(tabulate.tabulate(result, headers = headers))

    return result

# Orders table query needs fixing....

def retrieve_orders_table(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''
    SELECT * FROM orders;'''

    cursor.execute(sql)

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    
    headers = ('customer_id', 'customer_name', 'customer_addres', 'customer_phone')
    print('Total number of orders in the database: ' + str(cursor.rowcount))
    print('\n')
    print(tabulate.tabulate(result, headers = headers))

    return result

def insert_into_products(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''INSERT INTO products (product_name, product_price, product_stock)
    VALUES (%(product_name)s, %(product_price)s, %(product_stock)s);'''

    support_functions.clear()
    retrieve_products_table()

    try:
        product_name = input('\n' + 'What is the name of the product you would like to add? ')
        product_price = float(input('\n' + 'What is the price of the product you would like to add? '))
        product_stock = int(input('\n' + 'How many of this product are in stock? '))

        product_dict = {'product_name': product_name, 'product_price': product_price, 'product_stock': product_stock}

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

    sql = '''INSERT INTO couriers (courier_name, courier_phone)
    VALUES (%(courier_name)s, %(courier_phone)s);'''

    support_functions.clear()
    retrieve_couriers_table()

    courier_name = input('\n' + 'What is the name of the courier you would like to add? ')
    courier_phone = input('\n' + 'What is the phone number of the courier you would like to add? ')

    courier_dict = {'courier_name': courier_name, 'courier_phone': courier_phone}

    cursor.execute(sql, courier_dict)

    connection.commit()
    cursor.close()
    connection.close()

def insert_into_customers(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    sql = '''INSERT INTO customers (customer_name, customer_address, customer_phone)
    VALUES (%(customer_name)s, %(customer_address)s, %(customer_phone)s);'''

    support_functions.clear()
    retrieve_customers_table()

    customer_name = input('\n' + 'What is the name of the customer? ')
    customer_address = input('\n' + 'What is the customer\'s address? ')
    customer_phone = input('\n' + 'What is the customer\'s phone number? ')

    customer_dict = {'customer_name': customer_name, 'customer_address': customer_address, 'customer_phone': customer_phone}

    cursor.execute(sql, customer_dict)

    connection.commit()
    cursor.close()
    connection.close()

def get_product(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    cursor = connection.cursor()

    try:
        support_functions.clear()
        products = retrieve_products_table(database)
        print(products)
        product_selection = int(input('\n' + 'Please select the id of the product you would like to add to the order: '))
        
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

    sum = 0

    for i in range(len(price_tuple)):
        price = price_tuple[i][0]
        quantity = price_tuple[i][1]
        total = price * quantity
        sum += total

    return sum

def insert_into_orders(database = 'cafe_app'):
    connection = mysql.connect(host, user, password, database)

    try:
        product_list = []
        indicator = 0
        while indicator == 0:
            product_tuple = get_product(database)
            product_list.append(product_tuple)
            add_another_product = input('\n' + 'Would you like to add another product to the order? [Y/N] ')
            if add_another_product[0].lower() == 'y':
                continue
            else:
                indicator = 1

        support_functions.clear()
        retrieve_customers_table(database)
        customer_id = int(input(print_statements.customer_selection))
        support_functions.clear()
        retrieve_couriers_table(database)
        courier_id = int(input(print_statements.courier_selection))
    
        connection = mysql.connect(
        host,
        user,
        password,
        database
        )

        cursor = connection.cursor()
        transaction = '''START TRANSACTION;'''
        order = '''INSERT INTO orders (customer_id, courier_id, order_status_id)
        VALUES (%(customer_id)s, %(courier_id)s, %(order_status_id)s);'''

        order_dict = {'customer_id': customer_id, 'courier_id': courier_id, 'order_status_id': 1}

        cursor.execute(transaction)
        cursor.execute(order, order_dict)
        connection.commit()
        order_id = cursor.lastrowid

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

        order_total_cost = get_total_cost(order_id, database)

        cost = '''UPDATE orders 
        SET order_total_cost = %(order_total_cost)s
        WHERE order_id = %(order_id)s;'''
        print(cost)
        cost_dict = {'order_total_cost': order_total_cost, 'order_id': order_id}
        print(cost_dict)
        cursor.execute(cost, cost_dict)

        connection.commit()
        cursor.close()
        connection.close()
    
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
        print(print('\n'))
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
        print(print('\n'))
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
        select_courier = int(input(print_statements.update_selection))
        print(print('\n'))
        update_selection = int(input(print_statements.customer_update_options))

        if update_selection == 0:
            name_update = input('\n' + 'What would you like to update the customer name to? ')

            sql = '''UPDATE customers
            SET customer_name = %(name_update)s
            WHERE customer_id = %(select_courier)s;'''

            name_update_dict = {'name_update': name_update, 'select_courier': select_courier}

            cursor.execute(sql, name_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)

        elif update_selection == 1:
            address_update = input('\n' + 'What would you like to update the customer address to? ')

            sql = '''UPDATE customers
            SET customer_address = %(address_update)s
            WHERE customer_id = %(select_courier)s;'''

            address_update_dict = {'address_update': address_update, 'select_courier': select_courier}

            cursor.execute(sql, address_update_dict)
            print_record_num = cursor.rowcount, 'records updated.'
            print(print_record_num)
        elif update_selection == 2:
            phone_update = input('\n' + 'What would you like to update the customer phone number to? ')

            sql = '''UPDATE customers
            SET customer_phone = %(phone_update)s
            WHERE customer_id = %(select_courier)s;'''

            phone_update_dict = {'phone_update': phone_update, 'select_courier': select_courier}

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

    sql = '''DELETE FROM products
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

    sql = '''DELETE FROM couriers
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

    sql = '''DELETE FROM customers
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