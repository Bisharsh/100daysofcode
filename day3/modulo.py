print ('Which number do you want to check?')

check_number = int(input('Please enter the number that you want to check if its even or odd: '))
if check_number%2 == 0:
    print('It is an even number.')
else:
    print('It is an odd number')