#parrot = "Norwegian Blue"
#for character in parrot:
#    print(character)

#number = "9,223;372;036 854,775;807"
number = input("Please enter a series of numbers, using any separators you like: ")

separators = ""
#separators = number[1::4]

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))



"""
# Challenge

quote = " Alright, but apart from the Sanitation, the Medicine, Education, Wine,\
Public Order, Irrigation, Roads, the Fresh-Water System, \
and Public Health, what have the Romans ever done for us?"

capital =""
 
# Use a for loop and an if statement to print just the capitals in the quote above.
for letter in quote:
    if letter.isupper():
        capital += letter

print(capital)
"""
