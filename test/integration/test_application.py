import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from app import app


class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_home_content(self) -> None:
        response = self.app.get('/')
        self.assertTrue(b'Success' in response.data or b'Failure' in response.data)

    def test_upcoming_content(self) -> None:
        response = self.app.get('/upcoming')
        self.assertTrue(b'Falcon 9' in response.data)

    def test_past_content(self) -> None:
        response = self.app.get('/past')
        self.assertTrue(b'Falcon 9' in response.data)
