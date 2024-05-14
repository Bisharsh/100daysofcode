print("Welcome to tip calculator")

total_bill = int(input("What is the total bill? $"))

tip_percent = int(input("What is the tip you want to give? Enter 10, 12, 15: "))

tip_calulation = total_bill+(total_bill*(tip_percent/100))

splitwise = tip_calulation/int(input("Enter the number of friends to split"))

print("Your per person share would be: ", splitwise)
