import modules.support_functions as support_functions
import modules.print_statements as print_statements 
import file_handlers.sql_module as sql
from unittest.mock import patch, Mock
import datetime
import pymysql as mysql
import pytest
import unittest
import builtins

# Get today's date
date = datetime.datetime.now()
day = date.day
month = date.month
year = date.year
date_str = f'{day}/{month}/{year}'

# Create test environment
def test_create_test_environment():
    sql.create_test_environment('test')

# Test retrieve Functions
def test_retrieve_products_table():
    # Assemble
    expected = ((1, 'Coke', 1.25, 12), (2, 'Fanta', 0.75, 15), (3, 'Pepsi', 1.0, 20))

    # Act
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

def test_retrieve_couriers_table():
    # Assemble
    expected = ((1, 'Mike', '07459346523'), (2, 'Pete', '07459346523'), (3, 'Claire', '07459346523'))

    # Act
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

def test_retrieve_customers_table():
    # Assemble
    expected = ((1, 'Pete', 'Standard Avenue, Covenrty', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07457582365'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'))

    # Act
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

def test_retrieve_order_status_table():
    # Assemble
    expected = ((1, 'preparing'), (2, 'out-for-delivery'), (3, 'delivered'))

    # Act
    result = sql.retrieve_order_status_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [0, 0])
def test_retrieve_orders_table_order_id_without_cancelled_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 0])
def test_retrieve_orders_table_order_id_with_cancelled_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2},
    {'order_id': 3, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'cancelled', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [0, 1])
def test_retrieve_orders_table_status_id_without_cancelled_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [0, 2])
def test_retrieve_orders_table_courier_id_without_cancelled_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2},
    {'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [0, 5])
def test_retrieve_orders_table_incorrect_id_without_cancelled_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [5, 5])
def test_retrieve_orders_table_both_incorrect_ids(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2}]

    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = ['show', 'courier'])
def test_retrieve_orders_table_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

# Test insert into products
@patch('builtins.input', side_effect = ['Ham & Cheese Sandwich', 4.5, 7, 0])
def test_insert_into_products_valid(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 12), (2, 'Fanta', 0.75, 15), (3, 'Pepsi', 1.0, 20), (4, 'Ham & Cheese Sandwich', 4.5, 7))

    # Act
    sql.insert_into_products('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = ['Ham & Cheese Sandwich', 'Ham'])
def test_insert_into_products_price_string(mock_input: Mock):
    # Assemble
    expected = ValueError

    # Act
    result = sql.insert_into_products('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [7457595256, 3.2, 5])
def test_insert_into_products_name_int(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 12), (2, 'Fanta', 0.75, 15), (3, 'Pepsi', 1.0, 20), (4, 'Ham & Cheese Sandwich', 4.5, 7), (5, '7457595256', 3.2, 5))

    # Act
    sql.insert_into_products('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

# Test insert into couriers
@patch('builtins.input', side_effect = ['Jonny', '07457595256'])
def test_insert_into_couriers_valid(mock_input: Mock):
    # Assemble
    expected = ((1, 'Mike', '07459346523'), (2, 'Pete', '07459346523'), (3, 'Claire', '07459346523'), (4, 'Jonny', '07457595256'))

    # Act
    sql.insert_into_couriers('test')
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

# Test insert into customers
@patch('builtins.input', side_effect = ['Joe', 'Solihull, West Midlands', '07457595256'])
def test_insert_into_customers_valid(mock_input: Mock):
    # Assemble
    expected = ((1, 'Pete', 'Standard Avenue, Covenrty', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07457582365'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'),
    (4, 'Joe', 'Solihull, West Midlands', '07457595256'))

    # Act
    sql.insert_into_customers('test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

# Test get_product function
@patch('builtins.input', side_effect = [1, 2])
def test_get_product_valid(mock_input: Mock):
    # Assemble
    expected = (1, 2)

    # act
    result = sql.get_product('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 14])
def test_get_product_out_of_stock(mock_input: Mock):
    # Assemble
    expected = 'Insufficient stock error'

    # act
    result = sql.get_product('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [3, 'name'])
def test_get_product_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.get_product('test')

    # Assert
    assert expected == result

# Test get_total_cost function
def test_get_total_cost_valid():
    # Assemble 
    expected = 2.5

    # Act
    result = sql.get_total_cost(1, 'test')

    # Assert
    assert expected == result

# Test insert into orders
@patch('builtins.input', side_effect = [3, 2, 3, 2, 'n', 1, 0])
def test_insert_into_orders_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Fanta', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2},
    {'order_id': 3, 'customer_name': 'Kevin', 'courier_name': 'Mike', 'order_status': 'cancelled', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2}]

    # Act
    sql.insert_into_orders('test')
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 2, 3, 30, 'n'])
def test_insert_into_orders_out_of_stock(mock_input: Mock):
    # Assemble
    expected = 'Insufficient stock error'

    # Act
    
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 2, 7, 2, 'n'])
def test_insert_into_orders_incorrect_product(mock_input: Mock):
    # Assemble
    expected = 'Invalid product_id selection.'

    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [7, 2, 3, 2, 'n'])
def test_insert_into_orders_incorrect_customer(mock_input: Mock):
    # Assemble
    expected = 'Invalid customer selection.'

    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 7, 3, 2, 'n'])
def test_insert_into_orders_incorrect_courier(mock_input: Mock):
    # Assemble
    expected = 'Invalid courier selection.'

    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = ['num', 2, 3, 2, 'n'])
def test_insert_into_orders_value_error_one(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 'num', 3, 2, 'n'])
def test_insert_into_orders_value_error_two(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 2, 'num', 2, 'n'])
def test_insert_into_orders_value_error_three(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 2, 3, 'num', 'n'])
def test_insert_into_orders_value_error_four(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.insert_into_orders('test')

    # Assert
    assert expected == result

# Test update product function
@patch('builtins.input', side_effect = [2, 0, 'Sprite'])
def test_update_product_name(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 15), (3, 'Pepsi', 1.0, 18), (4, 'Ham & Cheese Sandwich', 4.5, 7), (5, '7457595256', 3.2, 5))

    # Act
    sql.update_product('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [3, 1, 0.75])
def test_update_product_price(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 15), (3, 'Pepsi', 0.75, 18), (4, 'Ham & Cheese Sandwich', 4.5, 7), (5, '7457595256', 3.2, 5))

    # Act
    sql.update_product('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [3, 2, 25])
def test_update_product_stock(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 15), (3, 'Pepsi', 0.75, 25), (4, 'Ham & Cheese Sandwich', 4.5, 7), (5, '7457595256', 3.2, 5))

    # Act
    sql.update_product('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', side_effect = [12, 2, 25])
def test_update_product_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records updated.'
    
    # Act
    sql.update_product('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.print')
@patch('builtins.input', side_effect = [3, 3, 25])
def test_update_product_incorrect_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = print_statements.error_statement
    
    # Act
    sql.update_product('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', side_effect = [3, 1, 'name'])
def test_update_product_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.update_product('test')

    # Assert
    assert expected == result

# Test update courier function
@patch('builtins.input', side_effect = [1, 0, 'Jason'])
def test_update_courier_name(mock_input: Mock):
    # Assemble
    expected = ((1, 'Jason', '07459346523'), (2, 'Pete', '07459346523'), (3, 'Claire', '07459346523'), (4, 'Jonny', '07457595256'))

    # Act
    sql.update_courier('test')
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 1, '07429246100'])
def test_update_courier_phone(mock_input: Mock):
    # Assemble
    expected = ((1, 'Jason', '07459346523'), (2, 'Pete', '07429246100'), (3, 'Claire', '07459346523'), (4, 'Jonny', '07457595256'))

    # Act
    sql.update_courier('test')
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', side_effect = [12, 1, '07429246100'])
def test_update_courier_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records updated.'
    
    # Act
    sql.update_courier('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.print')
@patch('builtins.input', side_effect = [3, 2, 'Jason'])
def test_update_courier_incorrect_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = print_statements.error_statement
    
    # Act
    sql.update_courier('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', side_effect = [3, 'name', 'name'])
def test_update_courier_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.update_courier('test')

    # Assert
    assert expected == result

# Test update customer function
@patch('builtins.input', side_effect = [4, 0, 'Jonathan'])
def test_update_customer_name(mock_input: Mock):
    # Assemble
    expected = ((1, 'Pete', 'Standard Avenue, Covenrty', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07457582365'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'),
    (4, 'Jonathan', 'Solihull, West Midlands', '07457595256'))

    # Act
    sql.update_customer('test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 1, 'Balsall Common, Warwickshire'])
def test_update_customer_address(mock_input: Mock):
    # Assemble
    expected = ((1, 'Pete', 'Balsall Common, Warwickshire', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07457582365'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'),
    (4, 'Jonathan', 'Solihull, West Midlands', '07457595256'))

    # Act
    sql.update_customer('test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [2, 2, '07550592850'])
def test_update_customer_phone(mock_input: Mock):
    # Assemble
    expected = ((1, 'Pete', 'Balsall Common, Warwickshire', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07550592850'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'),
    (4, 'Jonathan', 'Solihull, West Midlands', '07457595256'))

    # Act
    sql.update_customer('test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', side_effect = [12, 0, 'Jonathan'])
def test_update_customer_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records updated.'
    
    # Act
    sql.update_customer('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.print')
@patch('builtins.input', side_effect = [3, 3])
def test_update_customer_incorrect_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = print_statements.error_statement
    
    # Act
    sql.update_customer('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', side_effect = [3, 'name'])
def test_update_customer_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.update_customer('test')

    # Assert
    assert expected == result

# Test update_order function

@patch('builtins.input', side_effect = [1, 0, 3, 0, 3, 1, 0])
def test_update_order_customer_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Jason', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Sprite', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2.0},
    {'order_id': 3, 'customer_name': 'Claire', 'courier_name': 'Jason', 'order_status': 'cancelled', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.0},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2.0},
    {'order_id': 5, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 6, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 7, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 8, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0}]

    # Act
    sql.update_order('test')
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 0, 3, 1, 2, 2, 'n', 1, 0])
def test_update_order_products_valid(mock_input: Mock):
    # Assemble
    expected_orders = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Jason', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Sprite', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2.0},
    {'order_id': 3, 'customer_name': 'Claire', 'courier_name': 'Jason', 'order_status': 'cancelled', 'product_list': [{'product': 'Sprite', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 1.5},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2.0},
    {'order_id': 5, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 6, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 7, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 8, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0}]

    expected_product_orders = ((1, 1, 2),
    (2, 1, 1), 
    (2, 2, 1),
    (3, 2, 2),
    (4, 3, 2))

    expected_products = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 13), (3, 'Pepsi', 0.75, 27), (4, 'Ham & Cheese Sandwich', 4.5, 7), (5, '7457595256', 3.2, 5))

    # Act
    sql.update_order('test')
    result_orders = sql.retrieve_orders_table('test')

    host = 'localhost'
    user = 'root'
    password = 'password'
    connection = mysql.connect(host, user, password, 'test')
    cursor = connection.cursor()
    query = 'SELECT * FROM order_products;'
    cursor.execute(query)
    result_product_orders = cursor.fetchall()

    result_products = sql.retrieve_products_table('test')

    # Assert
    assert expected_orders == result_orders
    assert expected_product_orders == result_product_orders
    assert expected_products == result_products

@patch('builtins.input', side_effect = [1, 0, 3, 2, 2, 1, 0])
def test_update_order_courier_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Jason', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Sprite', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2.0},
    {'order_id': 3, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'cancelled', 'product_list': [{'product': 'Sprite', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 1.5},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2.0},
    {'order_id': 5, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 6, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 7, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 8, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0}]

    # Act
    sql.update_order('test')
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 0, 3, 3, 2, 1, 0])
def test_update_order_status_valid(mock_input: Mock):
    # Assemble
    expected = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Jason', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Sprite', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2.0},
    {'order_id': 3, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Sprite', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 1.5},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2.0},
    {'order_id': 5, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 6, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 7, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0},
    {'order_id': 8, 'customer_name': 'Kevin', 'courier_name': 'Pete', 'order_status': 'cancelled', 'date': date_str, 'order_total_cost': 0}]

    # Act
    sql.update_order('test')
    result = sql.retrieve_orders_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', side_effect = [1, 0, 12, 0, 0])
def test_update_order_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records updated.'
    
    # Act
    sql.update_order('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.print')
@patch('builtins.input', side_effect = [1, 0, 3, 7])
def test_update_order_incorrect_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = print_statements.error_statement
    
    # Act
    sql.update_order('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', side_effect = [1, 0, 3, 'name'])
def test_update_order_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.update_order('test')

    # Assert
    assert expected == result

# Test delete_product function
@patch('builtins.input', return_value = 5)
def test_delete_product_valid(mock_input: Mock):
    # Assemble
    expected = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 13), (3, 'Pepsi', 0.75, 27), (4, 'Ham & Cheese Sandwich', 4.5, 7))

    # Act
    sql.delete_product('test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 12)
def test_delete_product_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records deleted.'
    
    # Act
    sql.delete_product('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', return_value = 'Coke')
def test_delete_product_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.delete_product('test')

    # Assert
    assert expected == result

# Test delete_courier function
@patch('builtins.input', return_value = 1)
def test_delete_courier_valid(mock_input: Mock):
    # Assemble
    expected = ((2, 'Pete', '07429246100'), (3, 'Claire', '07459346523'), (4, 'Jonny', '07457595256'))

    # Act
    sql.delete_courier('test')
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 12)
def test_delete_courier_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records deleted.'
    
    # Act
    sql.delete_courier('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', return_value = 'Jonny')
def test_delete_courier_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.delete_courier('test')

    # Assert
    assert expected == result

# Test delete_customer function
@patch('builtins.input', return_value = 3)
def test_delete_customer_valid(mock_input: Mock):
    # Assemble
    expected = ((1, 'Pete', 'Balsall Common, Warwickshire', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07550592850'),
    (4, 'Jonathan', 'Solihull, West Midlands', '07457595256'))

    # Act
    sql.delete_customer('test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 12)
def test_delete_customer_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records deleted.'
    
    # Act
    sql.delete_customer('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', return_value = 'Jonny')
def test_delete_customer_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.delete_customer('test')

    # Assert
    assert expected == result

# Test cancel_order function
@patch('builtins.input', side_effect = [3, 0, 0])
def test_cancel_order_valid(mock_input: Mock):
    # Assemble
    expected_orders = [{'order_id': 1, 'customer_name': 'Pete', 'courier_name': 'Claire', 'order_status': 'preparing', 'product_list': [{'product': 'Coke', 'quantity': 2}], 'date':'26/10/2021', 'order_total_cost': 2.5},
    {'order_id': 2, 'customer_name': 'Kevin', 'courier_name': 'Jason', 'order_status': 'out-for-delivery', 'product_list': [{'product': 'Coke', 'quantity': 1}, {'product': 'Sprite', 'quantity': 1}], 'date':'26/10/2021', 'order_total_cost': 2},
    {'order_id': 4, 'customer_name': 'Claire', 'courier_name': 'Pete', 'order_status': 'preparing', 'product_list': [{'product': 'Pepsi', 'quantity': 2}], 'date': date_str, 'order_total_cost': 2}]

    expected_products = ((1, 'Coke', 1.25, 10), (2, 'Sprite', 0.75, 15), (3, 'Pepsi', 0.75, 27), (4, 'Ham & Cheese Sandwich', 4.5, 7))

    # Act
    sql.cancel_order('test')
    result_orders = sql.retrieve_orders_table('test')
    result_products = sql.retrieve_products_table('test')

    # Assert
    assert expected_orders == result_orders
    assert expected_products == result_products

@patch('builtins.print')
@patch('builtins.input', return_value = 12)
def test_cancel_order_incorrect_id(mock_input: Mock, mock_print: Mock):
    # Assemble
    expected = 0, 'records deleted.'
    
    # Act
    sql.cancel_order('test')

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', return_value = 'order')
def test_cancel_order_value_error(mock_input: Mock):
    # Assemble
    expected = ValueError
    
    # Act
    result = sql.cancel_order('test')

    # Assert
    assert expected == result

# Delete test environment
def test_delete_test_environment():
    sql.delete_test_environment('test')