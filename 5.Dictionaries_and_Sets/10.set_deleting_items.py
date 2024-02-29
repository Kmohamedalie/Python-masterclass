# *****************************************************************
#               deleting items from a set                         #
# *****************************************************************

small_ints = set(range(21))
print(small_ints)

# .clear() method
# small_ints.clear()
# print(small_ints)

# .discard() method
small_ints.discard(10)
small_ints.discard(10) # does not throw an error if it 's present
print(small_ints)

# .remove() method
small_ints.remove(11)
# small_ints.remove(11) # throw an error if it 's present
print(small_ints)
