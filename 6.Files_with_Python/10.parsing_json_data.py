# **********************************************************************
#                       Parsing JSON Data                              #
# **********************************************************************
import json

# practical application - parsing JSON data  (NOAA case)
json_data_source = "temperature_anomaly.json"

with open(json_data_source, encoding='utf-8') as data:
    anomalies = json.load(data)

print("description: ")
print(anomalies['description'])

print('citation: ')
print(anomalies['citation'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)
print('citation: ')
print(anomalies['citation'])
