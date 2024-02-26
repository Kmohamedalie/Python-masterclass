# *****************************************************
#                   replacing a slice                 #
# *****************************************************

computer_parts = ["computer", "monitor", "keyboard",
                  "mouse", "mouse mat"]

print("Original list: ")
print(computer_parts)

# test 0
computer_parts[3] = "trackball"
print(computer_parts[3:])

# test 1
computer_parts[3:] = "trackball"
print(computer_parts)

# test 2
computer_parts[3:] = ["trackball"]
print(computer_parts)

# test 3
computer_parts[3] = ["trackball"]
print(computer_parts)
