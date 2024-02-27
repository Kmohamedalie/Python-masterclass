# ************************************************
#                 sum odd or even                #
# ************************************************
def sum_eo(n,t):
    even = []  # empty list to store even values
    odd = []  # empty list to store odd values
    # even section (t==e)
    if t == "e":
        for e in range(1,n):
            if e%2 == 0:
                even.append(e)
        return sum(even)
    # odd section (t==o)
    elif t == "o":
        for i in range(1,n):
            if i%2 != 0:
                odd.append(i)
        return sum(odd)
    # every other value
    else:
        return -1


result = sum_eo(7,'o')
print(result)
