import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import data


class TestData(unittest.TestCase):
    def test_replace_launch_ids(self) -> None:
        launch_data = {
            'rocket': '5e9d0d95eda69973a809d1ec',
            'launchpad': '5e9e4501f5090910d4566f83'
        }
        launch = data.replace_launch_ids(launch_data)
        self.assertEqual(type(launch), dict)
        self.assertEqual(launch['rocket'], 'Falcon 9')
        self.assertEqual(launch['launchpad'], 'VAFB SLC 3W')

    def test_get_next_launch(self) -> None:
        launch = data.get_next_launch()
        self.assertEqual(type(launch), dict)
        self.assertTrue('fairings' in launch)

    def test_get_latest_launch(self) -> None:
        launch = data.get_latest_launch()
        self.assertEqual(type(launch), dict)
        self.assertTrue('fairings' in launch)

    def test_get_upcoming_launches(self) -> None:
        launches = data.get_upcoming_launches()
        self.assertEqual(type(launches), list)
        self.assertEqual(type(launches[0]), dict)
        self.assertTrue('fairings' in launches[0])

    def test_get_past_launches(self) -> None:
        launches = data.get_past_launches()
        self.assertEqual(type(launches), list)
        self.assertEqual(type(launches[0]), dict)
        self.assertTrue('fairings' in launches[0])
