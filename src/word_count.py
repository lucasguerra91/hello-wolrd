def count_words(filename):
    """"Count the appoximate number of words in a file. """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist. "
        #print(msg)
        # En lugar de pasar el mensaje de error, simplemente lo ignoramos
        pass
    else:
        # Count approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words. " )


filenames = ['alice.txt', 'tuvieja.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)