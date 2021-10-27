import file_handlers.csv_module as csv 
import file_handlers.sql_module as sql
from unittest.mock import patch, Mock
import pymysql as mysql

def test_create_test_environment():
    sql.create_test_environment('test')

def test_import_products_from_csv():
    # Assemble
    expected = ((1, 'Coke', 1.25, 12), (2, 'Fanta', 0.75, 15), (3, 'Pepsi', 1.0, 20), (4, 'Croissant', 0.75, 12), (5, 'Pain au Chocolat', 0.95, 12), (6, 'Sausage Roll', 1.2, 12))

    # Act
    csv.import_products_from_csv(products_filename = 'data/database_products_test_dataset.csv', database = 'test')
    result = sql.retrieve_products_table('test')

    # Assert
    assert expected == result

def test_import_couriers_from_csv():
    # Assemble
    expected = ((1, 'Mike', '07459346523'), (2, 'Pete', '07459346523'), (3, 'Claire', '07459346523'), (4, 'Jonathan', '07459346523'), (5, 'Sammy', '07459346523'), (6, 'Sharron', '07459346523'))

    # Act
    csv.import_couriers_from_csv(couriers_filename = 'data/database_couriers_test_dataset.csv', database = 'test')
    result = sql.retrieve_couriers_table('test')

    # Assert
    assert expected == result

def test_import_customers_from_csv():
    # Assemble
    expected = ((1, 'Pete', 'Standard Avenue, Covenrty', '07429246100'),
    (2, 'Kevin', 'Oxford Street, London', '07457582365'),
    (3, 'Claire', 'Balsall Common, Warwickshire', '07775505500'),
    (4, 'Jonathan', 'Piccadilly Circus', '07775505500'),
    (5, 'Adam', 'Birmingham', '07775505500'),
    (6, 'Kate', 'Knowle', '07775505500'))

    # Act
    csv.import_customers_from_csv(customers_filename = 'data/database_customers_test_dataset.csv', database = 'test')
    result = sql.retrieve_customers_table('test')

    # Assert
    assert expected == result

def test_delete_test_environment():
    sql.delete_test_environment('test')