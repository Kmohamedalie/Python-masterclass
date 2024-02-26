# ********************************************************************************
#                          selection from options                                #
# ********************************************************************************


options  = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
print("1.Learn Python \n2.Learn Java \n3.Go swimming \n4.Have dinner  \n5.Go to bed \n0.Exit ")

chosen = int(input("Please choose your option from the list below: "))
options_list = []
while chosen != 0:
    chosen = int(input("Please choose your option from the list below: "))
    if chosen in range(0,6):
      options_list.append(chosen)

print()
print("The following are the options: ")
for i in options_list:
    print("{}.{}".format(options.index(options[i]), options[i]))
