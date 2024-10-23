# Xavier Overs
import decode

def print_menu():
    """Prints the menu options"""
    print('\nMenu'
          '\n-------------'
          '\n1. Encode'
          '\n2. Decode'
          '\n3. Quit')


def encode(string):
    """take in an 8-digit password in string format containing only integers.
    After passing the password into the encoder, the encoder stores the encoded
    password to a new variable, with each digit being shifted up by 3 numbers."""

    encoded_string = ''  # declare global string variable

    for i in range(len(string)):
        if string[i] == '0':
            encoded_string += '3'
        if string[i] == '1':
            encoded_string += '4'
        if string[i] == '2':
            encoded_string += '5'
        if string[i] == '3':
            encoded_string += '6'
        if string[i] == '4':
            encoded_string += '7'
        if string[i] == '5':
            encoded_string += '8'
        if string[i] == '6':
            encoded_string += '9'
        if string[i] == '7':
            encoded_string += '0'
        if string[i] == '8':
            encoded_string += '1'
        if string[i] == '9':
            encoded_string += '2'

    return encoded_string


def main():
    user_menu_option = None

    while user_menu_option != '3':
        print_menu()
        user_menu_option = input('\nPlease enter an option: ')

        if user_menu_option == '1':
            user_password = input('Please enter your password to encode: ')
            if user_password:
                print('Your password has been encoded and stored!')

        if user_menu_option == '2':
            print(f'The encoded password is {encode(user_password)}, and the original password is {decode.decode(encode(user_password))}.')


if __name__ == '__main__':
    main()
