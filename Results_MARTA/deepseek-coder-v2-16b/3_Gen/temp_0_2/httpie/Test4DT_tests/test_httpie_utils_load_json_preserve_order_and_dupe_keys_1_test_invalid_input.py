
import json
from unittest.mock import patch, MagicMock
from httpie.utils import JsonDictPreservingDuplicateKeys

def load_json_preserve_order_and_dupe_keys(s):
    return json.loads(s, object_pairs_hook=JsonDictPreservingDuplicateKeys)

# Test case for invalid input
def test_invalid_input():
    s = '{"name": "John", "age": 30, "city": "New York"}'
    with patch('httpie.utils.json.loads', side_effect=ValueError("Invalid JSON")):
        try:
            load_json_preserve_order_and_dupe_keys(s)
        except ValueError as e:
            assert str(e) == "Invalid JSON"
