# *****************************************************
#              .split method                          #
# *****************************************************

# .split() : for splitting strings

panGram = "The quick brown fox jumps over the lazy dog"

words = panGram.split()
print(words)


numbers = "1,234,567,78,8,334,5566,608,807"
print(numbers.split(","))
new = []
for i in numbers.split(","):
    new.append(int(i))
print(new)

user = input("please enter three values a,b,c: ")
userList = user.split(",")
a = int(userList[0])
b = int(userList[1])
c = int(userList[2])
calc = a + b - c
print(calc)
