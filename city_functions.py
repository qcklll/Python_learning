def city (name, country, population):
    full_name = name + ',' + country + ' ' + str(population)
    return full_name.title()


print(city('kiev', 'ukraine',500000))