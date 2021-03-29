import unittest
from requests import get


class TestApi(unittest.TestCase):

    def test_next_status_code(self):
        response = get('https://api.spacexdata.com/v4/launches/next')
        self.assertEqual(response.status_code, 200)

    def test_latest_status_code(self):
        response = get('https://api.spacexdata.com/v4/launches/latest')
        self.assertEqual(response.status_code, 200)

    def test_upcoming_status_code(self):
        response = get('https://api.spacexdata.com/v4/launches/upcoming')
        self.assertEqual(response.status_code, 200)

    def test_past_status_code(self):
        response = get('https://api.spacexdata.com/v4/launches/past')
        self.assertEqual(response.status_code, 200)
