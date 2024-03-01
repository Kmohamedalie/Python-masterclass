# **********************************************************************
#                       CSV FORMAT                                     #
# **********************************************************************
# using the csv library
import csv

# csv_filename = "OlympicMedals_2020.csv"
csv_filename = "cereal_grains.csv"
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC) # note only for numeric
    for row in reader:
        print(row)

"""
# using the pandas library
import pandas as pd
olympics_data = pd.read_csv("OlympicMedals_2020.csv")
print(olympics_data)

cereal_grain_data = pd.read_csv("cereal_grains.csv")
print(cereal_grain_data)
"""
