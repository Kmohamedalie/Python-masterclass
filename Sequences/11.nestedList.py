# *****************************************************
#          Nested Lists & Code Style                  #
# *****************************************************

"""
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)
"""
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"]
]

"""
# processing nested lists
for meal in menu:
    if "spam" not in meal:
        print(meal)
        for subVal in range(len(meal)):
            print(meal[subVal])
    else:
        print("{} has a spam score of {}.".format(meal,meal.count("spam")))
"""

# remove spam in a list challenge
for meal in menu:
    while "spam" in meal:
        meal.remove("spam")
    # print(meal)
        # for subVal in range(len(meal)):
        #    print(meal[subVal])

    print("{} has a spam score of {}.".format(meal, meal.count("spam")))
