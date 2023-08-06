
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

def calculate_bmi(weight:int, height:float):
    try:
        bmi = int(weight) / (float(height)**2)
        print(int(bmi))
    except ValueError as ve:
        print(f"Error", ve)

# calculate_bmi(weight, height) 


#! FLOOR DIVISION
# print(8 // 3)


a = int("5") / int(2.7)
# print(type(a))


#! string formatting expression

number = 33.5
print("{:.2f}".format(number)) # this formats the float to print 2 digits after the decimal. 

num = 35
print("{:d}".format(num)) # formats an integer without decimals

large_num = 65198465651.15
print("{:e}".format(large_num))

print("{:.2g}") # this is a general format that chooses between fixed point and scientific notation. it will choose whichever is shorter

