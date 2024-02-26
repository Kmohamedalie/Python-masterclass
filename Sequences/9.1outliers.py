# *****************************************************
#                     outliers                        #
# *****************************************************

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)


# process the high values in the list
start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)
