# ********************************************************
#                   sorting                             #
# ********************************************************

# using the: sorted(value)

# example 1.
panGram = "The quick brown fox jumps over the lazy dog"

letters = sorted(panGram)
print("sorted panGram: ")
print(letters)

# example 2.
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)  # sorted doesn't mutate the original value
print("\nnumbers: ")
print(numbers)
print("\nsorted numbers: ")
print(sorted_numbers)

numbers.sort()  # mutate the original value
print()
print(".sort() method: ")
print(numbers)

another_numbers_sort = numbers.sort()  # doesn't return anything
print()
print("assigning the result to a variable .sort() method: ")
print(another_numbers_sort)

missing_letter = sorted("The quick brown fox jumps over the lazy dog.", key=str.casefold)
print()
print(missing_letter)

print(missing_letter)

# Case-Insensitive Sorting
names = ["Graham",
         "John",
         "terry",
         "eric",
         "michael"]

names.sort(key=str.casefold)
print()
print(names)
