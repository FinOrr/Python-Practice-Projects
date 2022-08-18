'''
Given a user input, this program will find and print all the prime factors of the number.
'''

def get_target_number():
    '''
    This function will get the target number from the user.
    '''
    target_number = int(input("Enter a number: "))
    return target_number

def get_prime_factors(target_number):
    '''
    This function will find all the prime factors of the target number.
    '''
    prime_factors = []
    for i in range(2, target_number):
        if target_number % i == 0:
            prime_factors.append(i)
    return prime_factors

def main():
    '''
    This is the main function.
    '''
    target_number = get_target_number()
    prime_factors = get_prime_factors(target_number)
    # print out the prime factors of the target number, if none are found then alert the user
    if len(prime_factors) == 0:
        print(f"No prime factors were found for {target_number}.")
    else:
        print(f"The prime factors of {target_number} are: {prime_factors}")

if __name__ == "__main__":
    main()