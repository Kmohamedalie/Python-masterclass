# *********************************************************************
#                  set intersection practice                          #
# *********************************************************************

# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}
print("using the .intersection(set): ")
print(farm_animals.intersection(wild_animals.intersection(potential_rides)))
print()
print("using the '&' for intersection: ")
intersection_ = farm_animals & wild_animals & potential_rides
print(intersection_)
print()
print("using  .intersection(set1, set2): ")
print(farm_animals.intersection(wild_animals, potential_rides))


# challenge
text = """Education is not the learning of facts
but the training of the mind to think
– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
text = set(text.split())
preps_used = text.intersection(prepositions)
print("The intersection: ")
print(preps_used)
