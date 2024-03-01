# ******************************************************
#              read, readline, readlines               #
# ******************************************************

"""
# readlines returns a list of strings
with open("Jabberwocky.txt", mode="r") as jabber:
    lines = jabber.readlines()

print(lines)
print(lines[-1:])
"""

# read
with open("Jabberwocky.txt", mode="r") as jabber:
    text = jabber.read()

# print(text)
"""
for character in reversed(text):
    print(character, end="")
"""

# .readline() method
with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)
