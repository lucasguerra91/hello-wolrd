with open('pi_digits.txt') as file_object:
    contents =  file_object.read()
    print(contents.rstrip())

print('\n')

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

# Making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


filename2 = 'pi_million_digits.txt'
with open(filename2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:60] + "... ")
print(len(pi_string))