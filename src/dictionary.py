alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print('\n\t Moviendo al alien \n')
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] += x_increment

print('New x-position: ' + str(alien_0['x_position']))

print('\n')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print('Borrando el atributo points')
del alien_0['points']
print(alien_0)

print('\n Otra forma de utilizar los diccionarios como objetos..')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(" Sarah's favorite language is " + favorite_languages['sarah'].title() + " .")


print('\nLooping an object')

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key , value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

print('\n Imprimiendo los lenguajes favoritos de estos fulanos: \n')
for n, l in favorite_languages.items():
    print(n.title() + "'s favorite language is :" + l.title() + " .")

print('\nImprimiendo solo los nombres: ')
for name in favorite_languages.keys():
    print(name.title())


