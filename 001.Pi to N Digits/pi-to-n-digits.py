'''
Calculate pi to n digits, as specified by the user.
'''
import math
import sys

def main():
    '''
    Main function.
    '''
    n = get_n()
    print(generate_pi(n))

def generate_pi(n):
    '''
    Given a user input, generate pi to n digits.
    '''
    pi = math.pi
    pi_str = str(pi)
    return pi_str[:n]

def get_n():
    '''
    Get user input for the number of digits to calculate pi to.
    '''
    n = int(input('Enter the number of digits to calculate pi to: '))
    return n

if __name__ == '__main__':
    main()