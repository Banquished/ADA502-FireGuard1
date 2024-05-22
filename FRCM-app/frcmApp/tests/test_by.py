# test_utils.py within the tests directory

from django.test import TestCase
from src.main import get_city

class GetCityTest(TestCase):
    def test_get_city(self):
        # You can mock the Nominatim response here to avoid external API calls during tests

        # Test with known coordinates
        latitude = "60.383"  #latitude for Bergen
        longitude = "5.3327"  #longitude for Bergen

        # Call the function you want to test
        city = get_city(latitude, longitude)

        # Check that the result is what you expect
        self.assertEqual(city, 'Bergen')

        # Add more test cases for different coordinates, including edge cases
