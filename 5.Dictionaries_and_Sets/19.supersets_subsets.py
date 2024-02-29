# *********************************************************************
#                  subsets and supersets                              #
# *********************************************************************

animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }

birds = {'Robin', 'Swallow', 'Wren'}
print()

# .issubset() and .issuperset() method
print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print("*" * 37)

print(f'animals is a subset of birds: {animals.issubset(birds)}')
print(f'birds is a superset of animals: {birds.issuperset(animals)}')

print("*" * 37)

# using operators "==", "<=", "<", ">"
print(birds <= animals)
print(birds < animals)

print('*' * 37)

garden_birds = {'Swallow', 'Wren', 'Robin'}

print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print('*' * 37)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds > more_birds)
