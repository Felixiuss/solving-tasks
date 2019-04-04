from Coursera.to_json import get_data
import unittest


class JsonTest(unittest.TestCase):

    def test_to_json(self):
        self.assertEqual(get_data(), '{"name": "Roman", "age": 35, "wight": 75}')
