# **********************************************************************
#       Parsing JSON Data from the internet urllib.request             #
# **********************************************************************
import json
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/1/1850-2024/data.json"

# practical application - parsing JSON data  (NOAA case)
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
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
