# **********************************************************************
#                          DictReader                                  #
# **********************************************************************

import csv

cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_filename:
    reader = csv.DictReader(cereals_filename)
    for row in reader:
        print(row)
