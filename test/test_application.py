import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from application import application


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()

    def test_home_status_code(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200)

    def test_upcoming_status_code(self):
        result = self.app.get('/upcoming') 
        self.assertEqual(result.status_code, 200)

    def test_past_status_code(self):
        result = self.app.get('/past') 
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get('/about') 
        self.assertEqual(result.status_code, 200)
