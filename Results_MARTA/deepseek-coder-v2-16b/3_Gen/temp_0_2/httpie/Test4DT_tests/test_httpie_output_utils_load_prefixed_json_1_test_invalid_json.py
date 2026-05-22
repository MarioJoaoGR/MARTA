
import pytest
from unittest.mock import patch
import json
from httpie.output.utils import load_prefixed_json, parse_prefixed_json, load_json_preserve_order_and_dupe_keys

def test_invalid_json():
    with patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys', side_effect=ValueError):
        with pytest.raises(ValueError):
            load_prefixed_json("invalid json string")
