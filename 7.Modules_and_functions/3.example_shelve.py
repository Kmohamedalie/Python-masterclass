# *********************************************************************
#                         shelve module                               #
# *********************************************************************

# module with most of the datatype(list) method
import shelve
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
       print(obj)
