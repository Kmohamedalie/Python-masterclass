# **********************************************************************
#                        unicode in python                             #
# **********************************************************************

with open("jabberwocky.txt", encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
