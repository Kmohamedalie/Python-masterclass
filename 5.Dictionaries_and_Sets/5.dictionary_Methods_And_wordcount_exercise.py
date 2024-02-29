# *****************************************************************************
#                  wordcount exercise and dict methods                        #
# *****************************************************************************

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
new_test = "".join(i for i in text if i.isalpha()).lower()
print("letter frequency to count in: ")
print(new_test)

print()

for i in range(len(new_test)):
    if new_test[i].casefold() not in word_count.keys():
        word_count[new_test[i]] = 1
    else:
        word_count[new_test[i]] = word_count[new_test[i]] + 1

print()

# Your code goes here ...
# Printing the dictionary
print(f"word count: ")
for letter, count in sorted(word_count.items()):
    print(letter, count)

print()

# .keys() method
print(".keys() method: ")
for key in word_count.keys():
    print(key, end=" ")

print()

# .value() method
print(".values() method: ")
for value in word_count.values():
    print(value, end=" ")
word_count.update({"k": 5})

print()

# print after .update()
print(".update() method new dict: ")
print(word_count)

print()

# d.fromkeys(dictionary, default_values) method
print(dict.fromkeys(word_count, 0))

print()

# .copy() method
print(".copy method: ")
new_word_count = word_count.copy()
print(f"A change in wordcount: ")
word_count["k"] = 3
print(word_count)
print("new_word_count still remains unchanged: ")
print(new_word_count)
