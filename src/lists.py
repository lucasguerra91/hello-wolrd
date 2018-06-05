from builtins import print

motorcycles = []
# agregando items a la lista
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')

print(motorcycles)

# insertando un item a la lista
motorcycles.insert(0, 'Ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# ultimo eliminado, tambien se puede marcar el indice de cual queremos borrar pop(i)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# remove , para borrar un valor especifico, ojo que solo borra la primer ocurrencia
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " +  too_expensive.title() + " is too expensive for me.")


# Sorting - ordenando las listas
print("\n\t-- Sorting -- \n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Lista original: ')
print(cars)
cars.sort()
print('\nLista ordenada: ')
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\n\tLista original')
print(cars)
cars.sort(reverse=True)
print('\nLista ordenada al reves')
print(cars)

# Sorting temporal con sorted
print('\n -- Listas ordenadas temporalmente --')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nEsta es la lista original : ")
print(cars)
print("\nEsta es la lista ordenada : ")
print(sorted(cars))

