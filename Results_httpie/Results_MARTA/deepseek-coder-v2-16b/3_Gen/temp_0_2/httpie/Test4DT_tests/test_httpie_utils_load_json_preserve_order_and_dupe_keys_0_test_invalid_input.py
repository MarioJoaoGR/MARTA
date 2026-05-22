
import json
from unittest import TestCase, mock
from httpie.utils import load_json_preserve_order_and_dupe_keys

class TestHttpieUtilsLoadJsonPreserveOrderAndDupeKeys(TestCase):
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            invalid_json = '{"name": "John", "age": 30, "city": "New York"'
            load_json_preserve_order_and_dupe_keys(invalid_json)
