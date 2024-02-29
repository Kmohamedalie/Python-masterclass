# *******************************************************
#               In with a dictionary                    #
# *******************************************************

available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

# empty list to add the parts
items_parts = []
# empty dictionary
computer_parts = {}
# set choice to None
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        # add item to the list
        if chosen_part not in items_parts:
            items_parts.append(chosen_part)
        # add item to the dictionary
        if (chosen_part not in computer_parts) and (chosen_part != None):
            computer_parts[current_choice] = chosen_part
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    current_choice = input("> ")

# items added to the list
print("The items added to the lists are: ")
print(items_parts)

# items added to the dictionary
print("The items added to the dictionary are: ")
print(computer_parts)
