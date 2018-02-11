import pandas as pd


def remove_shit(elemet):
    new = ''
    if '[' in elemet:
        index = elemet.index('[')
        new += elemet[0:index]
        return new.strip()
    else:
        return elemet


list_of_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

df = list_of_tables[2]

countries = [remove_shit(i) for i in df[1].tolist()]
gdp = df[2].tolist()

our_cities = []
our_countries = []

with open('city_country.txt') as file:
    header = next(file)
    for row in file:
        line = row.strip().split(',')
        this_city = line[0]
        this_country = line[1]
        if this_country != '':
            this_country = line[1][1:]
            if '\xa0' in this_country:
                this_country = this_country.replace('\xa0', '')
        our_cities.append(this_city)
        our_countries.append(this_country)

our_gdp = []
for i, country in enumerate(our_countries):
    if country in countries:
        country_index = countries.index(country)
        this_gdp = gdp[country_index]
        our_gdp.append(this_gdp)
    else:
        our_gdp.append('')

final_db = pd.DataFrame({'City': our_cities, 'Country': our_countries,
                         'GDP': our_gdp})

final_db.to_csv('GDP per country.csv')
