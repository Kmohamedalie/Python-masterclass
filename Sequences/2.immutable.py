# *****************************************************
#                     Immutable                       #
# *****************************************************

"""
int,  float,  bool (True and False): a subclass of int
str(string),  tuple,  frozenset,   bytes
"""

result = True
print("{}: ".format(result))
another_result = result
print(id(result))
print(id(another_result))

print()

result = False
print("{}: ".format(result))
another_result = result
print(id(result))
print(id(another_result))

print()

result = "Correct"
print("{}: ".format(result))
another_result = result
print(id(result))
print(id(another_result))

print()

result += "ish"
print("{}: ".format(result))
another_result = result
print(id(result))
print(id(another_result))
