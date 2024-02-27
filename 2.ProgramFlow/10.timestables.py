#****************************************
#   TimesTable  / Nested-For-Loop       #
#****************************************

print("The multiplication table:")

for i in range(1,13):
    for j in range(1,13):
        #print(f"{i} multiply by {j} = {i*j}")
        print("{0} times {1} is {2}".format(j, i, i * j))
    print()
