'''
Given a user's input dimensions and the cost per square metre of flooring, 
calculate the total cost of flooring.
'''

def main():
    '''
    Main function.
    '''
    length = float(input('Enter the length of the room: '))
    width = float(input('Enter the width of the room: '))
    cost = float(input('Enter the cost per square metre of flooring: '))
    total = length * width * cost
    print('The total cost of flooring is £{:.2f}'.format(total))

if __name__ == '__main__':
    main()