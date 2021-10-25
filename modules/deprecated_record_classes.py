from abc import ABC, abstractmethod
import modules.support_functions as support_functions
import modules.print_statements as print_statements 

class Record(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate_dict(self):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

class Product(Record):
    def __init__(self):
        super().__init__()
        self.product = {}
        self.get_product_details()
    
    def __repr__(self):
        name = self.product.get('product_name', 'Product has not yet been assigned a name.')
        price = self.product.get('product_price', 'Product has not yet been assigned a price.')
        return f'product_name: {name}, product_price: {price}'

    def get_product_details(self):
        self.product['product_name'] = input('What is the name of the product you would like to add? ')
        self.product['product_price'] = float(input('What is the price of the product you would like to add? '))
        return self.product

    def generate_dict(self):
        return self.product

class Courier(Record):
    def __init__(self):
        super().__init__()
        self.courier = {}
        self.get_courier_details()

    def __repr__(self):
        name = self.courier.get('courier_name', 'Courier has not yet been assigned a name.')
        phone = self.courier.get('courier_phone', 'Courier has not yet been assigned a phone number.')
        return f'courier_name: {name}, courier_phone: {phone}'

    def get_courier_details(self):
        name = input('What is the name of the courier you would like to add? ')
        phone = input('What is the phone number of the courier you would like to add? ')
        self.courier['courier_name'] = name
        self.courier['courier_phone'] = phone
        return self.courier

    def generate_dict(self):
        return self.courier

class Customer(Record):
    def __init__(self):
        super().__init__()
        self.customer = {}
        self.get_customer_details()

    def __repr__(self):
        name = self.customer.get('customer_name', 'Courier has not yet been assigned a name.')
        address = self.customer.get('customer_address', 'Courier has not yet been assigned a name.')
        phone = self.customer.get('customer_phone', 'Courier has not yet been assigned a phone number.')
        return f'customer_name: {name}, customer_address: {address}, customer_phone: {phone}'

    def get_customer_details(self):
        customer_name = input('What is the name of the customer? ')
        customer_address = input('What is the customer address? ')
        customer_phone = input('What is the customer\'s phone number? ')
        self.customer['customer_name'] = customer_name
        self.customer['customer_address'] = customer_address
        self.customer['customer_phone'] = customer_phone
        return self.customer

    def generate_dict(self):
        return self.customer

class Order(Record):
    def __init__(self, products, couriers, customers):
        super().__init__()
        self.products = products
        self.couriers = couriers
        self.customers = customers
        self.order = {}

    def __repr__(self):
        customer_name = self.order.get('customer_name', 'Courier has not yet been assigned a name.')
        customer_address = self.order.get('customer_address', 'Courier has not yet been assigned a name.')
        customer_phone = self.order.get('customer_phone', 'Courier has not yet been assigned a phone number.')
        product_order = self.order.get('product_order', 'Product order has not yet been assigned any items.')
        courier_name = self.order.get('courier_name', 'Courier has not yet been assigned a name.')
        courier_phone = self.order.get('courier_phone', 'Courier has not yet been assigned a phone number.')
        status = self.order.get('order_status', 'Order status has not yet been assigned.')
        return f'customer_name: {customer_name}, customer_address: {customer_address}, customer_phone: {customer_phone}, product_order: {product_order}, courier_name: {courier_name}, courier_phone: {courier_phone}, order_status: {status}'

    def get_order(self):
        self.order = support_functions.get_customer(self.order, self.customers)
        self.order = support_functions.get_products(self.order, self.products)
        self.order = support_functions.get_courier(self.order, self.couriers)
        self.order = support_functions.get_order_status(self.order)
        return self.order