
import json
from typing import Tuple
from unittest.mock import patch
from httpie.output.utils import load_prefixed_json, load_json_preserve_order_and_dupe_keys

def test_none_input():
    with patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys', side_effect=ValueError):
        try:
            result = load_prefixed_json('')
            assert result == ('', {})
        except ValueError as e:
            assert str(e) == 'Invalid JSON'
