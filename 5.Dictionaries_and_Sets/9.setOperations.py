# *****************************************************************
#                        Set Operations                           #
# *****************************************************************

# note just empty curly braces will create a dictionary
numbers = {}
print(numbers, type(numbers))

# create a set using *""
numbers = {*""}
print(numbers, type(numbers))

# create a set using {*{}}
numbers = {*{}}
print(numbers, type(numbers))

# using the set() method
numbers = set()
print(numbers, type(numbers))

# adding a value to a set
numbers.add(1)
print(numbers)

print()

# adding programmatically
print("Adding programmatically...")
while len(numbers) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers.add(next_value)
print(numbers)

print()

# using set to remove duplicates values
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_data = sorted(set(data))


# using word count to count duplicates
new_dict = {}
for word in data:
    if word in new_dict:
        new_dict[word] += 1
    else:
        new_dict[word] = 1

# iterate to get only duplicates
duplicates = {}
for key, value in new_dict.items():
    if value > 1:
        duplicates[key] = value

print("word count in dictionary...")
print(new_dict)
print()
print(f"we've remove all duplicates using set {duplicates} and remain just single values")
print(unique_data)
