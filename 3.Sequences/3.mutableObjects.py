# *****************************************************
#                mutable objects                     #
# *****************************************************

"""
list, dict, set Bytearray
"""
shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

print()

# concatenate another list
shopping_list += ["cookies"]
print(shopping_list, "\n")
print(id(shopping_list))
print(another_list)

# binding multiple names to a list
a = b = c = d = e = f = another_list
print(a, "\n")

print("Adding cream: ")
b.append("cream")
print(d)
