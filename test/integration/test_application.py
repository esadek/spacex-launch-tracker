import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from application import application


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()

    def test_home_content(self):
        result = self.app.get('/')
        self.assertTrue(b'Success' in result.data or b'Failure' in result.data)

    def test_upcoming_content(self):
        result = self.app.get('/upcoming')
        self.assertTrue(b'Falcon 9' in result.data)

    def test_past_content(self):
        result = self.app.get('/past')
        self.assertTrue(b'Falcon 9' in result.data)
