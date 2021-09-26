from modules.print_statements import *
from modules.support_functions import *

class App:
    def __init__(self):
        self.menu = []
        self.main_menu()
    
    def __repr__(self):
        return 'This is the app for the pop-up cafe. It is used to log and track orders.'

    def print_menu(self):
        '''Method that prints the menu.'''
        clear()
        print(self.menu)

    def add_menu_item(self):
        '''Method that adds a new item in the menu.'''
        clear()
        item_add = input('What is the name of product you would like to add to the menu? ')
        if item_add in self.menu:
            print(does_exist)
            self.product_menu()
        confirmation = input(confirmation_statement).lower()
        if confirmation[0] == 'y':
            self.menu.append(item_add)
        else:
            clear()
            self.product_menu()
        clear()
        print(success_statement)
        follow_up = input('Would you like to add another product? [Y/N] ').lower()
        if follow_up[0] == 'y':
            self.add_menu_item()
        return self.menu

    def update_menu_item(self):
        '''Method that updates products on the menu.'''
        clear()
        item_update = input('What is the product in the menu you would like to update? ')
        if item_update in self.menu:
            ind = self.menu.index(item_update)
        else:
            print(does_not_exist)
            self.product_menu()
        new_item = input('What would you like to update it with? ')
        confirmation = input(confirmation_statement).lower()
        if confirmation[0] == 'y':
            self.menu[ind] = new_item
        else:
            clear()
            self.product_menu()
        clear()
        print(success_statement)
        follow_up = input('Would you like to update another product? [Y/N] ').lower()
        if follow_up[0] == 'y':
            self.update_menu_item()
        return self.menu

    def delete_item(self):
        '''Method that deletes items from the menu.'''
        clear()
        item_delete = input('What is the product you would like to delete from the menu? ')
        if item_delete in self.menu:
            ind = self.menu.index(item_delete)
        else: 
            print(does_not_exist)
            self.product_menu()
        confirmation = input(confirmation_statement).lower()
        if confirmation[0] == 'y':
            self.menu.pop(ind)
        else:
            clear()
            self.product_menu()
        clear()
        print(success_statement)
        follow_up = input('Would you like to delete another product? [Y/N] ').lower()
        if follow_up[0] == 'y':
            self.delete_item()
        return self.menu

    def main_menu(self):
        '''Method that calls the main menu of the app.'''
        clear()
        print(main_menu_options)
        main_menu_input = int(input(input_statement))
        if main_menu_input == 0:
            clear()
            print(exit_statement)
            quit()
        elif main_menu_input == 1:
            clear()
            self.product_menu()
        else:
            clear()
            print(error_statement)
            self.main_menu()

    def product_menu(self):
        '''Method that calls the product menu of the app.'''
        print(product_menu_options)
        product_menu_input = int(input(input_statement))
        if product_menu_input == 0:
            print('Returning to main menu.')
            self.main_menu()
        elif product_menu_input == 1:
            self.print_menu()
            self.product_menu()
        elif product_menu_input == 2:
            self.add_menu_item()
            self.product_menu()
        elif product_menu_input == 3:
            self.update_menu_item()
            self.product_menu()
        elif product_menu_input == 4:
            self.delete_item()
            self.product_menu()
        else:
            print(error_statement)
            self.product_menu()

Cafe = App()