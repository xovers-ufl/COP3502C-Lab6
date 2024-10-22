def print_menu():
    """Prints the menu options"""
    print('Menu'
          '\n-------------'
          '\n1. Encode'
          '\n2. Decode'
          '\n3. Quit')


def encode():
    """increases every digit by 3"""
    pass


def decode():
    """decreases every digit by 3"""
    pass


def main():

    user_menu_option = None

    while user_menu_option != '3':
        print_menu()



        user_menu_option = input('Please enter an option: ')



if __name__ == '__main__':
    main()