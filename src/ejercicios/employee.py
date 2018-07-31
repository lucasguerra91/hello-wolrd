class Employee():
    """ Modelado de un empleado """

    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self):
        self.salary += 5000
        return self.salary

    def give_custom_raise(self, c_raise):
        self.salary += c_raise
        return self.salary
