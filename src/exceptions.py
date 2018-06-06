try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by Zero!")

# Ejemplo de try dentro de divisiones

print("Give me two numbers, and i will divide them")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by Zero!")
    else:
        print(answer)


# Ejemplo de try para file not found

filename = 'alice.txt'

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = "\n\nSorry, the file " + filename + " does not exist. "
    print(msg)
else:
    #Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + "has about " + str(num_words) + " words.")



# me quede en la pagina 204