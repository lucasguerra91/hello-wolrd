from cities_format import city_format

print("\n\tEnter 'q' at any time to quit.")
while True:
    city = input("\nInsert city : ")
    if city == 'q':
        break
    country = input("Insert country : ")
    if country == 'q':
        break

    population = input("Insert population (Empty if not) : ")
    if population == 'q':
        break

    full_name = city_format(city, country, population)
    print("\n\t Neatly formatted city name: " + full_name + ". ")
