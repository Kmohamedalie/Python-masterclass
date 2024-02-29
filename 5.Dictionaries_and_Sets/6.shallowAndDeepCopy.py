# **********************************************************************
#                       shallow and deep copy                          #
# **********************************************************************

lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

# shallow copy
# things = animals.copy()
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}
print("Shallow copy same ids: ")
print(id(things['teddy']), things["teddy"])
print(id(animals['teddy']), animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via 'animals'")
things["teddy"].append("added via 'things'")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)

# deep copy
import copy

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print()

things = copy.deepcopy(animals)
print("Deep copy different ids: ")
print(id(things['teddy']), things['teddy'])
print(id(animals['teddy']), animals['teddy'])

print()

# deep Copy function challenge
from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the 'list' or 'dict' values.

    The function will crash with an AttributeError if the values aren't
    list or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of 'd', with the values being copies of the original
    values.
    """
    # Your code goes here.
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


print("The result of the my_deepcopy: ")
recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])

print()
original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]]
}

copy_1 = copy.deepcopy(original)  # inbuilt
copy_2 = my_deepcopy(original)  # created

# add values
original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(f"Original: {original}")
print(f"copy_1: {copy_1}")
print(f"copy_2: {copy_2}")
