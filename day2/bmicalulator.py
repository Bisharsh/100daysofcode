height = input("please enter your height: ")
weight = input("please enter your weight: ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int/height_as_float ** 2
print(int(bmi))
