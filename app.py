from print_statements import *

class App:
    def __init__(self):
        self.menu = []
    
    def __repr__(self):
        return 'This is the app for the pop-up cafe. It is used to log and track orders.'

    def add_menu_item(self,item_add):
        self.menu.append(item_add)
        print(success_statement)
        return self.menu
    
    def print_menu(self):
        print('\n')
        print(self.menu)

    def update_menu_item(self, item_update, new_item):
        ind = self.menu.index(item_update)
        self.menu[ind] = new_item
        print(success_statement)
        return self.menu

    def delete_item(self, item_delete):
        ind = self.menu.index(item_delete)
        self.menu.pop(ind)
        print(success_statement)
        return self.menu

    def customer_input(self):
        inp_one = None
        while inp_one != 0:
            print(main_menu_options)
            inp_one = int(input(input_statement))
            if inp_one == 0:
                print(exit_statement)
            elif inp_one == 1:
                inp_two = None
                while inp_two != 0:
                    print(product_menu_options)
                    inp_two = int(input(input_statement))
                    if inp_two == 0:
                        print('Returning to main menu.')
                        break
                    elif inp_two == 1:
                        self.print_menu()
                    elif inp_two == 2:
                        item_add = input('What is the name of product you would like to add to the menu? ')
                        self.add_menu_item(item_add)
                        print(success_statement)
                    elif inp_two == 3:
                        item_update = input('What is the product in the menu you would like to update? ')
                        new_item = input('What would you like to update it with? ')
                        self.update_menu_item(item_update, new_item)
                    elif inp_two == 4:
                        item_delete = input('What is the product you would like to delete from the menu? ')
                        self.delete_item(item_delete)
                    else:
                        print(error_statement)
                        inp_two = int(input(input_statement))
            else:
                print(error_statement)

Cafe = App()

Cafe.customer_input()