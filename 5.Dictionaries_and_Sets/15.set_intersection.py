# *********************************************************************
#                  set intersection method                            #
# *********************************************************************
from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print()
print("The intersection between odds and squares:")
print(odds.intersection(squares))
print("The intersection between even and squares:")
print(evens & squares)

# pass an iterable to the method
print("Passing and iterable: ")
even_squares = evens.intersection(squares_generator(100))
print(even_squares)
