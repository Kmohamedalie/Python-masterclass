# ********************************************************
#                 list methods                           #
# ********************************************************

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

"""
min, max, len, .append(value),


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# min - max ***************************************
print("\nmin and max method: ")
print("minimum value for even is: {}".format(min(even)))
print("maximum value for even is: {}\n".format(max(even)))

print("minimum value for odd is: {}".format(min(odd)))
print("maximum value for odd is: {}".format(max(odd)))

# len **********************************************
print("\nlen method: ")
print("length for odd is: {}".format(len(odd)))
print("length for even is: {}\n".format(len(even)))

# count **********************************************
# word = input("Enter a word: ")
# letters = input("Enter the letters to count: ")
# print("{} appears {} times in {}.".format(letters,word.count(letters),word))

# append **********************************************
print("\n.append() method: ")

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]
current_choice = "_"
computer_parts = []  # create and empty list

while current_choice != "0":
    if current_choice in "1234567":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "2":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "3":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "4":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "5":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "6":
            computer_parts.append(available_parts[int(current_choice)-1])
        elif current_choice == "7":
            computer_parts.append(available_parts[int(current_choice)-1])
    else:
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()

print(computer_parts)
"""

# sorting **********************************************
print("*********** .extend() method:")
even.extend(odd) # .extend()
print(even)
another_even = even
print(another_even)

print("\n*********** .sort() method:")
even.sort(reverse=True)# .sort()
print(even)
print(another_even)
