# ********************************************************
#                enumerate function                      #
# ********************************************************
"""
enumerate: gets the item and it index value.
"""

print("\n.append() method: ")

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)] # list comprehension
print("valid choices: ", valid_choices)

current_choice = "_"
computer_parts = []  # create and empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
          # it's already in, so remove it
          print("Removing {}".format(current_choice))
          computer_parts.remove(chosen_part)
        else:
          computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)

# simple enumerate program
# for index, character in enumerate("abcdefgh"):
#    print(index, character)
