from modules.print_statements import *

class App:
    def __init__(self):
        self.menu = []
        self.main_menu()
    
    def __repr__(self):
        return 'This is the app for the pop-up cafe. It is used to log and track orders.'

    def add_menu_item(self):
        '''Method that adds a new item in the menu.'''
        item_add = input('What is the name of product you would like to add to the menu? ')
        self.menu.append(item_add)
        print(success_statement)
        return self.menu
    
    def print_menu(self):
        '''Method that prints the menu.'''
        print('\n')
        print(self.menu)

    def update_menu_item(self):
        '''Method that updates products on the menu.'''
        item_update = input('What is the product in the menu you would like to update? ')
        new_item = input('What would you like to update it with? ')
        ind = self.menu.index(item_update)
        self.menu[ind] = new_item
        print(success_statement)
        return self.menu

    def delete_item(self):
        '''Method that deletes items from the menu.'''
        item_delete = input('What is the product you would like to delete from the menu? ')
        ind = self.menu.index(item_delete)
        self.menu.pop(ind)
        print(success_statement)
        return self.menu

    def main_menu(self):
        '''Method that calls the main menu of the app.'''
        print(main_menu_options)
        main_menu_input = int(input(input_statement))
        if main_menu_input == 0:
            quit()
        elif main_menu_input == 1:
            self.product_menu()
        else:
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