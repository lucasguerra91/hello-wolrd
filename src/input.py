message = input("tell me something, and I will repeat it back to you: ")
print(message)

age =  input('How old are you? : ')
age = int(age)
# print(type(age)) con esto logramos que sea entero
if age > 18 :
    print('\nYou can vote !')
else:
    print('You cant vote')

# Functions
def greet_user(username):
    """ Display a simple greeting.""" # Descripcion de la funcion
    print("\n Hello, " + username.title() + "!")

greet_user('Lucas')

