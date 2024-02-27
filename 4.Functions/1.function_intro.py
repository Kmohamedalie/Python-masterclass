# ***************************************************************
#                      functions                                #
# ***************************************************************

def multipy(x: float, y: float) -> float:  # function annotation
    result = x * y
    return result


answer = multipy(6, 7)

print(answer)

print()

for val in range(1, 5):
    two_times = multipy(2, val)
    print(two_times)
