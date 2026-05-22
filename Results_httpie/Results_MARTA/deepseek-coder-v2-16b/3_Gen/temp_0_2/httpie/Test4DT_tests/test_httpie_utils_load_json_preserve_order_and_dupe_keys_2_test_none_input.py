
import json
from httpie.utils import load_json_preserve_order_and_dupe_keys, JsonDictPreservingDuplicateKeys
import unittest.mock as mock

def test_none_input():
    with mock.patch('httpie.utils.json.loads') as mock_loads:
        mock_loads.return_value = {}  # Replace this with the expected return value for your specific case
        s = None
        result = load_json_preserve_order_and_dupe_keys(s)
        assert result == {}, f"Expected an empty dictionary, but got {result}"
