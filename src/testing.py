import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_name_lastname(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        pass

    def test_middle_name(self):
        """uso de segundo nombre"""
        formatted_name = get_formatted_name('Lucas', 'Guerra', 'Gabriel')
        self.assertEqual(formatted_name, 'Lucas Gabriel Guerra')
        pass


if __name__ == '__main__':
    unittest.main()