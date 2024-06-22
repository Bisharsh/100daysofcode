print('thank you for choosing Pizza delivery!')
size = input("Enter the size of the pizza you want - S, M or L: ")
add_pepperoni = input('Want pepperoni? Y or N ')
extra_cheese = input('Want extra cheese? Y or N ')

price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
        if extra_cheese == "Y":
            price += 1
    elif extra_cheese == "Y":
        price += 1
    else: 
        price = 15

elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 2
        if extra_cheese == "Y":
            price += 1
    elif extra_cheese == "Y":
        price += 1
    else: 
        price = 20

else:
    price = 25
    if add_pepperoni == "Y":
        price += 2
        if extra_cheese == "Y":
            price += 1
    elif extra_cheese == "Y":
        price += 1
    else: 
        price = 25        