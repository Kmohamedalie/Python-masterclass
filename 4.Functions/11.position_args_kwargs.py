# *******************************************************************
#        positional arguments, *args, **kwargs                      #
# *******************************************************************

def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional:..........{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


# run the function
func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)


# challenge Variable number of arguments
def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print()


# run sum_numbers(*args)
print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
