import modules.print_statements as print_statements
import modules.support_functions as support_functions
import file_handlers.txt_module as txt
import file_handlers.json_module as json

class App():
    def __init__(self) -> None:
        self.products = txt.products_init()
        self.couriers = txt.couriers_init()
        self.orders = json.orders_init()
        self.main_menu()
    
    def __repr__(self):
        return 'This is the app for the pop-up cafe. It is used to log and track products, orders and couriers.'

    def print_record(self, record):
        '''Method that prints the menu.'''
        support_functions.clear()
        if record == 'product':
            print(self.products)
        elif record == 'courier':
            print(self.couriers)
        elif record == 'order':
            print(self.orders)

    def add_record(self, record):
        '''Method that adds a new record.'''
        support_functions.clear()
        if record == 'product':
            item_add = input('What is the name of product you would like to add to the menu? ')
            if item_add in self.products:
                print(print_statements.does_exist)
                self.product_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.products.append(item_add)
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to add another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.add_record('product')
            return self.products
        elif record == 'courier':
            courier_add = input('What is the name of the courier you would like to add? ')
            if courier_add in self.couriers:
                print(print_statements.does_exist)
                self.courier_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.couriers.append(courier_add)
            else:
                support_functions.clear()
                self.courier_menu()
            support_functions.clear()
            follow_up = input('Would you like to add another courier? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.add_record('courier')
            return self.couriers
        elif record == 'order':
            order_number = int(list(self.orders)[-1]) + 1
            customer_name, customer_address, customer_phone = support_functions.get_customer_details()
            product_order = support_functions.get_product_order(self.products)
            courier_details = support_functions.get_courier_details(self.couriers)
            order_status = support_functions.get_order_status()
            self.orders[order_number] = support_functions.order_dict(customer_name, customer_address, customer_phone, product_order, courier_details, order_status)
            support_functions.clear()
            follow_up = input('Would you like to create another order? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.add_record('order')
            return self.orders

    def update_record(self, record):
        '''Method that updates a record.'''
        support_functions.clear()
        if record == 'product':
            item_update = input('What is the product in the menu you would like to update? ')
            if item_update in self.products:
                ind = self.products.index(item_update)
            else:
                print(print_statements.does_not_exist)
                self.product_menu()
            new_item = input('What would you like to update it with? ')
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.products[ind] = new_item
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to update another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.update_record('product')
            return self.products
        elif record == 'courier':
            item_update = input('What is the courier in the list you would like to update? ')
            if item_update in self.couriers:
                ind = self.couriers.index(item_update)
            else:
                print(print_statements.does_not_exist)
                self.courier_menu()
            new_item = input('What would you like to update the courier with? ')
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.couriers[ind] = new_item
            else:
                support_functions.clear()
                self.courier_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to update another courier? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.update_record('courier')
            return self.couriers
        elif record == 'order':
            print(self.orders)
            order_number = int(input('Please select the order number you would like to update. '))
            if self.orders.get(order_number) is not None and order_number != 0:
                support_functions.clear()
                item_update = int(input(print_statements.order_update_options)) 
                if item_update == 0:
                    print(self.orders[order_number]['customer_name'])
                    name_update = input('What would you like to update the customer name to? ')
                    self.orders[order_number]['customer_name'] = name_update
                    print(print_statements.success_statement)
                elif item_update == 1:
                    print(self.orders[order_number]['customer_address'])
                    address_update = input('What would you like to update the customer address to? ')
                    self.orders[order_number]['customer_address'] = address_update
                    print(print_statements.success_statement)
                elif item_update == 2:
                    print(self.orders[order_number]['customer_phone'])
                    phone_update = input('What would you like to update the customer phone number to? ')
                    self.orders[order_number]['customer_phone'] = phone_update
                    print(print_statements.success_statement)
                elif item_update == 3:
                    print('The current order is ' + str(self.orders[order_number]['product_order']) + ' What would you like the new order to be?' )
                    product_update = support_functions.get_product_order(self.products)
                    self.orders[order_number]['product_order'] = product_update
                    print(print_statements.success_statement)
                elif item_update == 4:
                    print('The current courier is ' + self.orders[order_number]['courier'] + '. What would you like to change the courier to?')
                    courier_update = support_functions.get_courier_details(self.couriers)
                    self.orders[order_number]['courier'] = courier_update
                    print(print_statements.success_statement)
                elif item_update == 5:
                    print('The current order status is: "' + self.orders[order_number]['status'] + '". What would you like to update the status to?')
                    status_update = support_functions.get_order_status()
                    self.orders[order_number]['status'] = status_update
                    print(print_statements.success_statement)
                else:
                    print(print_statements.error_statement)
                    self.update_record('order')
            else:
                print('The order number you selected does not exist. Please select a valid order number.')
                self.update_record('order')
            return self.orders

    def delete_record(self, record):
        '''Method that deletes a record.'''
        support_functions.clear()
        if record == 'product':
            item_delete = input('What is the product you would like to delete from the menu? ')
            if item_delete in self.products:
                ind = self.products.index(item_delete)
            else: 
                print(print_statements.does_not_exist)
                self.product_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.products.pop(ind)
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to delete another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.delete_record('product')
            return self.products
        elif record == 'courier':
            item_delete = input('Which courier record would you like to delete from the list? ')
            if item_delete in self.couriers:
                ind = self.couriers.index(item_delete)
            else: 
                print(print_statements.does_not_exist)
                self.courier_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.couriers.pop(ind)
            else:
                support_functions.clear()
                self.courier_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to delete another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.delete_record('courier')
            return self.products
        elif record == 'order':
            print(self.orders)
            order_number = int(input('Please select the order number you would like to delete. '))
            if self.orders.get(order_number) is not None and order_number != 0:
                support_functions.clear()
                confirmation = input(print_statements.confirmation_statement).lower()
                if confirmation[0] == 'y':
                    self.orders.pop(order_number)
                else:
                    support_functions.clear()
                    self.order_menu()
                support_functions.clear()
                print(print_statements.success_statement)
            else:
                print('The order number you selected does not exist. Please select a valid order number.')
                self.delete_record('order')
            return self.products


    def main_menu(self):
        '''Method that calls the main menu of the app.'''
        support_functions.clear()
        print(print_statements.main_menu_options)
        main_menu_input = int(input(print_statements.input_statement))
        if main_menu_input == 0:
            support_functions.clear()
            txt.products_update(self.products)
            txt.couriers_update(self.couriers)
            json.orders_update(self.orders)
            print(print_statements.exit_statement)
            quit()
        elif main_menu_input == 1:
            support_functions.clear()
            self.product_menu()
        elif main_menu_input == 2:
            support_functions.clear()
            self.courier_menu()
        elif main_menu_input == 3:
            support_functions.clear()
            self.order_menu()
        else:
            support_functions.clear()
            print(print_statements.error_statement)
            self.main_menu()

    def product_menu(self):
        '''Method that calls the product menu of the app.'''
        print(print_statements.product_menu_options)
        product_menu_input = int(input(print_statements.input_statement))
        if product_menu_input == 0:
            print('Returning to main menu.')
            txt.products_update(self.products)
            self.main_menu()
        elif product_menu_input == 1:
            self.print_record('product')
            self.product_menu()
        elif product_menu_input == 2:
            self.add_record('product')
            self.product_menu()
        elif product_menu_input == 3:
            self.update_record('product')
            self.product_menu()
        elif product_menu_input == 4:
            self.delete_record('product')
            self.product_menu()
        else:
            print(print_statements.error_statement)
            self.product_menu()

    def courier_menu(self):
        '''Method that calls the courier menu of the app.'''
        print(print_statements.courier_menu_options)
        courier_menu_input = int(input(print_statements.input_statement))
        if courier_menu_input == 0:
            print('Returning to main menu.')
            txt.couriers_update(self.couriers)
            self.main_menu()
        elif courier_menu_input == 1:
            self.print_record('courier')
            self.courier_menu()
        elif courier_menu_input == 2:
            self.add_record('courier')
            self.courier_menu()
        elif courier_menu_input == 3:
            self.update_record('courier')
            self.courier_menu()
        elif courier_menu_input == 4:
            self.delete_record('courier')
            self.courier_menu()
        else:
            print(print_statements.error_statement)
            self.courier_menu()

    def order_menu(self):
        '''Method that calls the order menu of the app'''
        print(print_statements.order_menu_options)
        order_menu_input = int(input(print_statements.input_statement))
        if order_menu_input == 0:
            print('Returning to main menu.')
            json.orders_update(self.orders)
            self.main_menu()
        elif order_menu_input == 1:
            self.print_record('order')
            self.order_menu()
        elif order_menu_input == 2:
            self.add_record('order')
            self.order_menu()
        elif order_menu_input == 3:
            self.update_record('order')
            self.order_menu()
        elif order_menu_input == 4:
            self.delete_record('order')
            self.order_menu()
        else:
            print(print_statements.error_statement)
            self.order_menu()


cafe = App()