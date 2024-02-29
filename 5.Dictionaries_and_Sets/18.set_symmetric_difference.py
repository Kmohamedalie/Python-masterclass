# *********************************************************************
#               set symmetric difference                              #
# *********************************************************************

morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

possible_courses = morning ^ afternoon
print("The prime of both: ")
print(possible_courses)

print()

morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]
possible_courses = set(morning).symmetric_difference(afternoon)
print("symmetric difference on lists: ")
print(possible_courses)
