from pathlib import Path

def menu_init():
    menu = []
    f = Path('data\menu.txt')
    f.touch(exist_ok=True)
    with open('data\menu.txt', 'r+') as menu_file:
        for product in menu_file.readlines():
            menu.append(product.rstrip('\n'))
    menu_file.close()
    return menu 

def couriers_init():
    couriers = []
    f = Path('data\couriers.txt')
    f.touch(exist_ok=True)
    with open('data\couriers.txt', 'r+') as courier_file:
        for courier in courier_file.readlines():
            couriers.append(courier.rstrip('\n'))
    courier_file.close()
    return couriers

def menu_update(menu):
    with open('data\menu.txt', 'w+') as menu_file:
        for product in menu:
            menu_file.write(product + '\n')
    menu_file.close()

def couriers_update(couriers):
    with open('data\couriers.txt', 'w+') as courier_file:
        for courier in couriers:
            courier_file.write(courier + '\n')
    courier_file.close()