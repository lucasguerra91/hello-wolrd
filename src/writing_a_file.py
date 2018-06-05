# Leyendo, escribiendo y creando archivos

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


filename2 = 'guest.txt'
filename3 = 'reasons.txt'
message = 'yes'

# No es el mejor ejemplo de un while, pero es lo que me acuerdo
while message !='no':
    name = input("Whats your name?: ")
    with open(filename2, 'a') as file_object:
        file_object.write(name.title() +"\n")
    reason = input("Welcome, " + name + ".\nWhy you like programming..? :")
    with open(filename3, 'a') as file_object:
        file_object.write(reason.title() + "\n")
    message = input('Continue ? yes/no')



# Exceptions



