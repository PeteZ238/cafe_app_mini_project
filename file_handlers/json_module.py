from pathlib import Path
import json

def orders_init():
    if Path('data\orders.json').exists() == False:
        orders_init = {0: 'Cafe App Orders'}
        with open('data\orders.json', 'w+') as order_file:
            json.dump(orders_init, order_file, ensure_ascii = False, indent = 4)
        order_file.close()
    
    with open('data\orders.json', 'r+') as order_file:
        orders = json.load(order_file)
    order_file.close()    
    return orders

def orders_update(orders):
    with open('data\orders.json', 'w+') as order_file:
        json.dump(orders, order_file, ensure_ascii = False, indent = 4)