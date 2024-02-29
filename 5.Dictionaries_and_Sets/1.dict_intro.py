# *******************************************************
#               Intro to dictionary                     #
# *******************************************************

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# iterate on the vehicles
print("Iterating on vehicles dictionary: ")
for key, value in vehicles.items():
    print("{}: {}".format(key, value))

# adding values to a dictionary
vehicles['Ferrari'] = "Puro Sangue"
vehicles['starfighter'] = "Lockheed F-104"
vehicles["toy"] = "glider"

print()

# iterate on the vehicles
print("Iterating after adding {}, {} and {}: ".format(vehicles['Ferrari'], vehicles['starfighter'], vehicles['toy']))
for key, value in vehicles.items():
    print("{}: {}".format(key, value))

print()

# iterate on the vehicles
vehicles['starfighter'] = "F-16 fighter jet"
print("Iterating after changing {}: ".format(vehicles['starfighter']))
for key, value in vehicles.items():
    print("{}: {}".format(key, value))

print()

# .get('str') method
learner = vehicles.get("er5")
print(learner)

print()

# deleting values .pop('key') / it also returns a value
toy = vehicles.pop('toy')
print("The .pop method removes the value {}".format(toy))
print(vehicles)
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)

print()

# deleting values del dict['key']
del vehicles['starfighter']
print(vehicles)
