
import pytest
from unittest.mock import patch
import json
from httpie.output.utils import load_prefixed_json, parse_prefixed_json, load_json_preserve_order_and_dupe_keys

def test_invalid_json():
    data = 'Invalid JSON'
    with pytest.raises(ValueError):
        load_prefixed_json(data)
