
import unittest.mock as mock
from httpie.output.utils import load_prefixed_json, load_json_preserve_order_and_dupe_keys

def test_none_input():
    with mock.patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys', side_effect=ValueError("Invalid JSON")):
        data = ""
        try:
            result = load_prefixed_json(data)
            assert result == ('', {})
        except ValueError as e:
            assert str(e) == "Invalid JSON"
