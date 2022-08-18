'''
The program will output a prime number and ask the user if they want to continue.
If the user accepts, the next prime number will be output.
If the user declines, the program will output all the found prime numbers and exit.
'''

def generate_next_prime_number(current_prime_number):
    '''
    This function will generate the next prime number.
    '''
    next_prime_number = current_prime_number + 1
    while not is_prime_number(next_prime_number):
        next_prime_number += 1
    return next_prime_number

def is_prime_number(number):
    '''
    This function will check if the number is prime.
    '''
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_user_input():
    '''
    This function will get the user input.
    '''
    user_input = input("Do you want to continue? (y/n): ")
    return user_input

def main():
    '''
    This is the main function.
    '''
    current_prime_number = 2
    while True:
        print(current_prime_number)
        user_input = get_user_input()
        if user_input == "y":
            current_prime_number = generate_next_prime_number(current_prime_number)
        else:
            # If the user declines, the program will output all the found prime numbers and exit.
            index = 0
            print("All prime numbers found:")
            for i in range(2, current_prime_number + 1):
                if is_prime_number(i):
                    index += 1
                    print(f"[{index}]: {i}")
            break

if __name__ == "__main__":
    main()
