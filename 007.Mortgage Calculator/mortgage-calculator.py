'''
Calculate the monthly payments of a fixed term mortgage over given N
payments at a given interest rate. Also figure out how long it will take the
user to pay back the loan. For added complexity, add an option for users to
select the compounding interval (e.g. monthly, weekly, daily, etc.).
'''

def main():
    '''
    Main function.
    '''
    # Get user input for principal amt, interest rate (%), number of payments, and compounding interval.
    principal = float(input('Enter the principal: '))
    interest = float(input('Enter the interest rate (%): '))
    payments = int(input('Enter the number of payments: '))
    interval = input('Enter the compounding interval (annual,monthly, weekly, daily): ')
    
    if interval == 'annual':
        pass
    elif interval == 'monthly':
        interest /= 12
        payments *= 12
    elif interval == 'weekly':
        interest /= 52
        payments *= 52
    elif interval == 'daily':
        interest /= 365
        payments *= 365
    else:
        print('Invalid interval')
        return
    
    # Calculate the monthly payments
    monthly_payment = (principal * interest) / (1 - (1 + interest) ** -payments)
    # Output this to the user
    print('The monthly payment is £{:.2f}'.format(monthly_payment))
    # Output the number of payments the user will have to make
    print('It will take {} payments to pay back the loan'.format(payments))

if __name__ == '__main__':
    main()
    exit()