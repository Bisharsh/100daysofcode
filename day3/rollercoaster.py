print ('Welcome to the Rollercoaster!!')
height = int(input('What is your height in cm? '))
age = int(input('Please enter your age: '))

if height >= 120:
    print('You can ride the rollercoaster!!')
    if age > 12:
        print('Please pay $5 at the counter.')
    elif age > 18:
        print('Please pay $7')
    else:
        print('Please pay $12')
else:
    print('You have to grow taller before you can ride.')