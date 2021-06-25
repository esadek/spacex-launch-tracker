import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from app import app


class TestRouting(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_home_status_code(self) -> None:
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_upcoming_status_code(self) -> None:
        result = self.app.get('/upcoming')
        self.assertEqual(result.status_code, 200)

    def test_past_status_code(self) -> None:
        result = self.app.get('/past')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self) -> None:
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)
