# *********************************************************************
#                  set .union() and | method                          #
# *********************************************************************

"""
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# the .union() method
all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

# the pipe method " | "
all_animals_3 = wild_animals | farm_animals
print(all_animals_3)

print(all_animals_1 == all_animals_2 == all_animals_3)
"""

from prescription_data import adverse_interactions

meds_to_watch = set()
"""
for interaction in adverse_interactions:
    # .union(set) method
    # meds_to_watch = meds_to_watch.union(interaction)
    # the pipe operator
    # meds_to_watch = meds_to_watch | interaction
    # .update() method
    meds_to_watch |= interaction
"""
# unpacking
meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))

print()

# unpacking
print(*sorted(meds_to_watch), sep='\n')
