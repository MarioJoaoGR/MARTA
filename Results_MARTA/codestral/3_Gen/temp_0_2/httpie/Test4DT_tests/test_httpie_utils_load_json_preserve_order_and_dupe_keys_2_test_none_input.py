
import json
from httpie.utils import load_json_preserve_order_and_dupe_keys, JsonDictPreservingDuplicateKeys
import pytest

def test_none_input():
    s = None
    with pytest.raises(TypeError):
        result = load_json_preserve_order_and_dupe_keys(s)
