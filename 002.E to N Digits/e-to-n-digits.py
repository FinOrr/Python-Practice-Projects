'''
Get a user to input a number of digits, then generate e to that many decimal places
'''

import math
import decimal

def get_number_of_digits():
    '''
    Get a user to input a number of digits, then generate e to that many decimal places
    '''
    number_of_digits = int(input('Enter a number of digits: '))
    return number_of_digits

def generate_e(number_of_digits):
    '''
    Generate e to the number of digits
    '''
    e = math.e
    e_to_n_digits = round(e, number_of_digits)
    return e_to_n_digits

def main():
    '''
    Main function
    '''
    number_of_digits = get_number_of_digits()
    e_to_n_digits = generate_e(number_of_digits)
    print(e_to_n_digits)

if __name__ == '__main__':
    main()