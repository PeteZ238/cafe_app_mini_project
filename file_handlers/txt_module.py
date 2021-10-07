from pathlib import Path

def products_init():
    products = []
    f = Path('data\products.txt')
    f.touch(exist_ok = True)
    with open('data\products.txt', 'r+') as product_file:
        for product in product_file.readlines():
            products.append(product.rstrip('\n'))
    product_file.close()
    return products 

def couriers_init():
    couriers = []
    f = Path('data\couriers.txt')
    f.touch(exist_ok = True)
    with open('data\couriers.txt', 'r+') as courier_file:
        for courier in courier_file.readlines():
            couriers.append(courier.rstrip('\n'))
    courier_file.close()
    return couriers

def products_update(products):
    with open('data\products.txt', 'w+') as product_file:
        for product in products:
            product_file.write(product + '\n')
    product_file.close()

def couriers_update(couriers):
    with open('data\couriers.txt', 'w+') as courier_file:
        for courier in couriers:
            courier_file.write(courier + '\n')
    courier_file.close()