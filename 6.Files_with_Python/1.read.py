# ******************************************************
#                         read                         #
# ******************************************************

# .open() method to load the file in the variable jabber
jabber = open("Jabberwocky.txt")

# iterate in jabber using a forloop
for line in jabber:
    print(line, end='')
    # print(line.strip())
    # .rstrip(), .lstrip()
    # print(len(line))

# .close() to close the file and avoid and
# file corruption
jabber.close()
