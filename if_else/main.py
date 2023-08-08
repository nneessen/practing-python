#! IF ELSE NOTES

#! BASIC EXAMPLE 1
# print(f"Welcome to the rollercoaser!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoast!")
# else:
#     print("You're not tall enough to ride. Sorry!")


#! EXAMPLE 2 - nested if / elif / else
# print(f"Welcome to the rollercoaser!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoast!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5")
#     elif age < 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("You're not tall enough to ride. Sorry!")


#! EXAMPLE 3 - CHECKING IF A YEAR IS A LEAP YEAR

year = int(input("What year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")