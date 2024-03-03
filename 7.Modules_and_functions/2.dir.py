# *********************************************************************
#                         dir module                                  #
# *********************************************************************

# directory module
print("Items in the 'dir': ")
for index, _ in enumerate(dir()):
    print(f'{index+1}.', _.strip("__"))

count = 0
for _ in dir( __builtins__):
    print(_)
    count += 1
print(f"\nTotal modules: {count}")
