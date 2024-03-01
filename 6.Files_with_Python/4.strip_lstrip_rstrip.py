# ******************************************************
#                 strip, lstrip, rstrip                #
# ******************************************************

# custom made remove prefix function
def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # Return a copy of `string`.

# custom made remove suffix function
def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):  # suffix='' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]

filename = "jabberwocky.txt"
with open(filename, mode="r") as poem:
    first = poem.readline().rstrip()

chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:  # process backwards
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

# the following codes works only in python 3.9 and above
# removing prefix and suffix
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, 'toves')
print(toves_removed)
