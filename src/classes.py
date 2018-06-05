class Dog():
    """A simple attenmpt to model a dog."""

    def __init__(self, name , age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting .")

    def roll_over(self):
        print(self.name.title() + " rolled over! .")


# Making an instance

my_dog = Dog('Thor', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

# Calling methods
print("\nSentate..!")
my_dog.sit()
print("\n Roda..!")
my_dog.roll_over()
