'''
Start with a number n>1. Find the number of steps it takes to reach 1 by following these rules:
    > If n is even, divide n by 2.
    > If n is odd, multiply n by 3 and add 1.
    > Repeat the process until n = 1.
'''

def collatz(n):
    # Initialise the steps counter
    steps = 0
    # While n is not 1, continue to follow the rules
    while n != 1:
        # If n is even, divide n by 2
        if n % 2 == 0:
            n = n / 2
        # If n is odd, multiply n by 3 and add 1
        else:
            n = n * 3 + 1
        # Increment the steps counter
        steps += 1
    return steps

def main():
    n = int(input("Please enter a an initial starting value: "))
    print(f"The number of steps required is: {collatz(n)}")
    input()

if __name__ == '__main__':
    main()
    exit()