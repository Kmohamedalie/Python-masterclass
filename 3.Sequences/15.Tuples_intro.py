# *****************************************************
#                Tuples                               #
# *****************************************************

t = "a", "b", "c"
v = ("a", "b", "c")
print(type(t))
print(t)
print(t == v)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print()
print(metallica)
print(metallica[0])
print(metallica[1])

# TypeError: 'tuple' object does not support item assignment
# metallica[3] = "Master of puppets"

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of puppets"
print(metallica2)

print()
# more tuple unpacking
title, artist, year = metallica
print(title)
print(artist)
print(year)

print()
table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

print()
name, length, width, height, price = table
print(length * width)
