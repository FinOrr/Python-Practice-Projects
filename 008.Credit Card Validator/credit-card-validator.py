'''
Credit card validator uses the Luhn algorithm to generate a checksum
and ensure the credit card number input by the user is valid.
'''

# Generate the luhn algorithm for the input credit card number: n
def luhn_algorithm(n):
    # Reverse the credit card number: n
    n = [int(i) for i in n[::-1]]
    # Loop through every other digit, starting from the end
    for i in range(1, len(n), 2):
        # Double the current digit
        n[i] *= 2
        # If the doubled digit is greater than 9, subtract 9 from the doubled digit
        if n[i] > 9:
            n[i] -= 9
    # If the modulus of the sum of the digits is 0, return True (valid card number)
    return sum(n) % 10 == 0

def main():
    card_number = str(input("Please enter your credit card number: "))
    if luhn_algorithm(card_number):
        print("This card number is valid.")
    else:
        print("Error! Invalid card number.")

if __name__ == '__main__': 
    main()
    input()
    exit()