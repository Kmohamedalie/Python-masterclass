# **********************************************************************************
#            parsing data in a text file (country's -capital                       #
# **********************************************************************************
input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline() # read the first line(headings)
    # iterate over the remaining data
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict  # lookup using country name
        countries[code.casefold()] = country_dict  # lookup using iso code

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country/iso code: ').casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
