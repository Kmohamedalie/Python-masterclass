# ***********************************************
#         using and, or, in Conditions          #
# ***********************************************

age = int(input("How old are you? "))
print("-" * 27)

# and ******************************
# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("-" * 27)


# or *******************************
if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")
print("-" * 27)


# in & range ***********************
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
