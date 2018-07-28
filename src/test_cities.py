import unittest
from cities_format import city_format


class CityTestCase (unittest.TestCase):
    """ Test cities.py """

    def test_city_country(self):
        """Se verifica formateo de ciudad , pais"""
        formatted_city = city_format('Buenos Aires', 'Argentina')
        self.assertEqual(formatted_city, 'Buenos Aires, Argentina')
        pass

    def test_population(self):
        """ se verifica si acepta el campo poblacion"""
        formatted_city = city_format('Buenos Aires', 'Argentina', '2300000')
        self.assertEqual(formatted_city, 'Buenos Aires, Argentina - population : 2300000')
        pass


if __name__ == '__main__':
    unittest.main()