import modules.support_functions as support_functions
import modules.print_statements as print_statements 
from unittest.mock import patch, Mock
import pytest
import unittest
import builtins

@patch('builtins.input', return_value = 2)
def test_delete_record_happy(mock_input: Mock):
    # Assemble
    input_list = [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}]
    expected = [{1: 'a'}, {2: 'b'}, {4: 'd'}]

    # Act
    result = support_functions.delete_record(input_list)

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 5)
def test_delete_record_corner(mock_input: Mock, mock_print: Mock):
    # Assemble
    input_list = [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}]
    expected = '\n' + 'Invalid option, please select a valid option.'

    # Act
    result = support_functions.delete_record(input_list)

    # Assert
    mock_print.assert_called_with(expected)

@patch('builtins.input', side_effect = [1, 0, 'Pepsi'])
def test_update_product_name(mock_input: Mock):
    # Assemble
    product_list = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Coke', 'product_price': 0.75}, {'product_name': 'Sprite', 'product_price': 0.6}]
    expected = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Pepsi', 'product_price': 0.75}, {'product_name': 'Sprite', 'product_price': 0.6}]

    # Act
    result = support_functions.update_product(product_list)

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 1, 1])
def test_update_product_price(mock_input: Mock):
    # Assemble
    product_list = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Coke', 'product_price': 0.75}, {'product_name': 'Sprite', 'product_price': 0.6}]
    expected = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Coke', 'product_price': 1}, {'product_name': 'Sprite', 'product_price': 0.6}]

    # Act
    result = support_functions.update_product(product_list)

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 3)
def test_update_product_incorrect_product_index(mock_input: Mock, mock_print: Mock):
    # Assemble
    product_list = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Coke', 'product_price': 0.75}, {'product_name': 'Sprite', 'product_price': 0.6}]
    
    # Act
    support_functions.update_product(product_list)

    # Assert
    mock_print.assert_called_with(print_statements.error_statement)

@patch('builtins.print')
@patch('builtins.input', side_effect = [1, 2])
def test_update_product_incorrect_product_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    product_list = [{'product_name': 'Fanta', 'product_price': 0.5}, {'product_name': 'Coke', 'product_price': 0.75}, {'product_name': 'Sprite', 'product_price': 0.6}]
    
    # Act
    support_functions.update_product(product_list)

    # Assert
    mock_print.assert_called_with(print_statements.error_statement)

# Test update product non integer input for both layers (select from list and select which property to update)

@patch('builtins.input', side_effect = [1, 0, 'Francisco'])
def test_update_courier_name(mock_input: Mock):
    # Assemble
    courier_list = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Pete', 'courier_phone': '07459346523'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]
    expected = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Francisco', 'courier_phone': '07459346523'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]

    # Act
    result = support_functions.update_courier(courier_list)

    # Assert
    assert expected == result

@patch('builtins.input', side_effect = [1, 1, '07429246100'])
def test_update_courier_phone(mock_input: Mock):
    # Assemble
    courier_list = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Pete', 'courier_phone': '07459346523'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]
    expected = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Pete', 'courier_phone': '07429246100'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]

    # Act
    result = support_functions.update_courier(courier_list)

    # Assert
    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 3)
def test_update_courier_incorrect_courier_index(mock_input: Mock, mock_print: Mock):
    # Assemble
    courier_list = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Pete', 'courier_phone': '07459346523'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]

    # Act
    support_functions.update_courier(courier_list)

    # Assert
    mock_print.assert_called_with(print_statements.error_statement)

@patch('builtins.print')
@patch('builtins.input', side_effect = [1, 2])
def test_update_courier_incorrect_courier_property(mock_input: Mock, mock_print: Mock):
    # Assemble
    courier_list = [{'courier_name': 'Mike', 'courier_phone': '07459346523'}, {'courier_name': 'Pete', 'courier_phone': '07459346523'}, {'courier_name': 'Claire', 'courier_phone': '07459346523'}]

    # Act
    support_functions.update_courier(courier_list)

    # Assert
    mock_print.assert_called_with(print_statements.error_statement)

# Test update product non integer input for both layers (select from list and select which property to update)

@patch('builtins.input', side_effect = [1, 0, 'Sharon'])
def test_update_customer_name(mock_input: Mock):
    customer_list = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    expected = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Sharon', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    result = support_functions.update_customer(customer_list)

    assert expected == result

@patch('builtins.input', side_effect = [1, 1, 'Picadilly Circus, London'])
def test_update_customer_address(mock_input: Mock):
    customer_list = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    expected = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Picadilly Circus, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    result = support_functions.update_customer(customer_list)

    assert expected == result

@patch('builtins.input', side_effect = [1, 2, '07828384850'])
def test_update_customer_phone(mock_input: Mock):
    customer_list = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    expected = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07828384850'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    result = support_functions.update_customer(customer_list)

    assert expected == result

@patch('builtins.print')
@patch('builtins.input', return_value = 3)
def test_update_customer_phone_incorrect_customer_index(mock_input: Mock, mock_print: Mock):
    customer_list = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    support_functions.update_customer(customer_list)

    mock_print.assert_called_with(print_statements.error_statement)

@patch('builtins.print')
@patch('builtins.input', side_effect = [1, 3])
def test_update_customer_phone_incorrect_customer_property(mock_input: Mock, mock_print: Mock):
    customer_list = [
        {'customer_name': 'Pete', 'customer_address': 'Standard Avenue, Covenrty', 'customer_phone': '07429246100'},
        {'customer_name': 'Kevin', 'customer_address': 'Oxford Street, London', 'customer_phone': '07457582365'},
        {'customer_name': 'Claire', 'customer_address': 'Balsall Common, Warwickshire', 'customer_phone': '07775505500'}
    ]

    support_functions.update_customer(customer_list)

    mock_print.assert_called_with(print_statements.error_statement)

# Test update customer non integer input for both layers (select from list and select which property to update)

