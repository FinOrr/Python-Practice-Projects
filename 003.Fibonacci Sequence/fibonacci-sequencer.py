import math
import decimal

'''
User inputs a number, then generates the fibonacci sequence with that many iterations
'''

def get_input():
    '''
    Get a user to input a number of iterations, then generate the fibonacci sequence with that many iterations
    '''
    number_of_iterations = int(input('Enter a number of iterations: '))
    return number_of_iterations

def generate_fibonacci_sequence(number_of_iterations):
    '''
    Generate the fibonacci sequence with the number of iterations
    '''
    fibonacci_sequence = [1, 1]
    for i in range(number_of_iterations - 2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def main():
    '''
    Main function
    '''
    number_of_iterations = get_input()
    fibonacci_sequence = generate_fibonacci_sequence(number_of_iterations)
    print(fibonacci_sequence)

if __name__ == '__main__':
    main()