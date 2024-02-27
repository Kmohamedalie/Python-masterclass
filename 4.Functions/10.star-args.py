# ******************************************************************
#                        star-args (*args)                         #
# ******************************************************************

numbers = (0, 1, 2, 3, 4, 5)

print(numbers)
print(*numbers)
print(0, 1, 2, 3, 4, 5)
print(numbers, sep=";")
print(*numbers, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")

print()
def test_start(*args):
    print(args)
    for x in args:
        print(x)

# run test_start with arguments/parameters
test_start(0, 1, 2, 3, 4, 5)

print()

# run test_start with no parameter
test_start()
