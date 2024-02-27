# *****************************************************
#          Deleting Items from a list                 #
# *****************************************************

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# note after deleting the first two values the list only has 16 remaining
# del data[16:]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200
highLow = []

# deleting values less than the minimum or greater than the maximum (outliers)
for i in data:
    if i > max_valid or i < min_valid:
        pass
    else:
        highLow.append(i)

print(highLow)


stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)
