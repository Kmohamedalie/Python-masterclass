# **********************************************************************
#                     writing data to a text file                      #
# **********************************************************************

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = "flowers_write.txt"

# writing data in to file
with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

# writing int in to a file using print() method
filename = 'test_numbers.txt'
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# writing int in to a file using write() method
# Note: using write will throw an error since str is expected
with open(filename, "w") as test:
    for i in range(10):
        # test.write(i)
        test.write(str(i))
