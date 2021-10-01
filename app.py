import modules.print_statements as print_statements
import modules.support_functions as support_functions
import file_handlers.txt_module as txt

class App:
    def __init__(self) -> None:
        self.menu = txt.menu_init()
        self.couriers = txt.couriers_init()
        self.main_menu()
    
    def __repr__(self):
        return 'This is the app for the pop-up cafe. It is used to log and track products, orders and couriers.'

    def print_menu(self, record):
        '''Method that prints the menu.'''
        support_functions.clear()
        if record == 'menu':
            print(self.menu)
        elif record == 'courier':
            print(self.couriers)

    def add_menu_item(self, record):
        '''Method that adds a new item in the menu.'''
        support_functions.clear()
        if record == 'menu':
            item_add = input('What is the name of product you would like to add to the menu? ')
            if item_add in self.menu:
                print(print_statements.does_exist)
                self.product_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.menu.append(item_add)
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to add another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.add_menu_item('menu')
            return self.menu
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
                self.add_menu_item('courier')

    def update_menu_item(self, record):
        '''Method that updates products on the menu.'''
        support_functions.clear()
        if record == 'menu':
            item_update = input('What is the product in the menu you would like to update? ')
            if item_update in self.menu:
                ind = self.menu.index(item_update)
            else:
                print(print_statements.does_not_exist)
                self.product_menu()
            new_item = input('What would you like to update it with? ')
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.menu[ind] = new_item
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to update another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.update_menu_item('menu')
            return self.menu
        elif record == 'courier':
            item_update = input('What is the pcourier in the list you would like to update? ')
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
                self.update_menu_item('courier')
            return self.couriers

    def delete_item(self, record):
        '''Method that deletes items from the menu.'''
        support_functions.clear()
        if record == 'menu':
            item_delete = input('What is the product you would like to delete from the menu? ')
            if item_delete in self.menu:
                ind = self.menu.index(item_delete)
            else: 
                print(print_statements.does_not_exist)
                self.product_menu()
            confirmation = input(print_statements.confirmation_statement).lower()
            if confirmation[0] == 'y':
                self.menu.pop(ind)
            else:
                support_functions.clear()
                self.product_menu()
            support_functions.clear()
            print(print_statements.success_statement)
            follow_up = input('Would you like to delete another product? [Y/N] ').lower()
            if follow_up[0] == 'y':
                self.delete_item('menu')
            return self.menu
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
                self.delete_item('courier')
            return self.menu


    def main_menu(self):
        '''Method that calls the main menu of the app.'''
        support_functions.clear()
        print(print_statements.main_menu_options)
        main_menu_input = int(input(print_statements.input_statement))
        if main_menu_input == 0:
            support_functions.clear()
            txt.menu_update(self.menu)
            txt.couriers_update(self.couriers)
            print(print_statements.exit_statement)
            quit()
        elif main_menu_input == 1:
            support_functions.clear()
            self.product_menu()
        elif main_menu_input == 2:
            support_functions.clear()
            self.courier_menu()
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
            self.main_menu()
        elif product_menu_input == 1:
            self.print_menu('menu')
            self.product_menu()
        elif product_menu_input == 2:
            self.add_menu_item('menu')
            self.product_menu()
        elif product_menu_input == 3:
            self.update_menu_item('menu')
            self.product_menu()
        elif product_menu_input == 4:
            self.delete_item('menu')
            self.product_menu()
        else:
            print(print_statements.error_statement)
            self.product_menu()

    def courier_menu(self):
        '''Method that calls the courier menu of the app.'''
        print(print_statements.courier_options)
        courier_menu_input = int(input(print_statements.input_statement))
        if courier_menu_input == 0:
            print('Returning to main menu.')
            self.main_menu()
        elif courier_menu_input == 1:
            self.print_menu('courier')
            self.courier_menu()
        elif courier_menu_input == 2:
            self.add_menu_item('courier')
            self.courier_menu()
        elif courier_menu_input == 3:
            self.update_menu_item('courier')
            self.courier_menu()
        elif courier_menu_input == 4:
            self.delete_item('courier')
            self.courier_menu()
        else:
            print(print_statements.error_statement)
            self.courier_menu()

cafe = App()