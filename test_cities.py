import unittest
from city_functions import city

class TestCity(unittest.TestCase):

    def test_city_country(self):
        right_name = city('kiev', 'ukraine', 'population=500000')
        self.assertEqual(right_name, 'Kiev,Ukraine Population=500000')


unittest.main()