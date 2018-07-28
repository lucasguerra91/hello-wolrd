def city_format (city, country, population=''):
    """Formateo de ciudad país"""
    if population:
        full_city_name = city + ', ' + country + ' - population : ' + population
    else:
        full_city_name = city + ', ' + country
    return full_city_name