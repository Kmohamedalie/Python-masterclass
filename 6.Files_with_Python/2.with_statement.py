# ******************************************************
#                  with statement                      #
# ******************************************************
print("Let's learn something about files: ")

with open("Jabberwocky.txt", mode="r") as jabber:
    # file = jabber.readline(10)
    for line in jabber:
        print(line.rstrip())
