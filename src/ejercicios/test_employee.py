import unittest
from .employee import Employee

class TestEmployee(unittest.TestCase):
    """ Probando los metodos de la clase empleado """

    def setUp(self):
        """ Instanciando la clase para pruebas """
        self.employee = Employee('Lucas', 'Guerra', 45000)

    def test_give_raise(self):
        self.assertEqual(self.employee.give_raise(), 50000)



if __name__ == '__main__':
    unittest.main()
