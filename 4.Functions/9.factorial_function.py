# ******************************************************************
#                        factorial                                 #
# ******************************************************************

def factorial(n: int) -> int:
    """
    The function factorial performs simple mathematical factorial
    :param n: number to be entered
    :return: n*(n-1)
    """
    #  print("{}!:".format(n))
    empty = []
    result = 1
    for i in range(n+1):
        if i == 0:
            i = 1
            empty.append(i)
        else:
            empty.append(i)
    for k in empty:
        result = result * k
    return result


# print the factorial of the values
for i in range(0,36):
    print("{} {}".format(i, factorial(i)))
