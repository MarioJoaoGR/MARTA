
import pytest
from dataclasses_json.core import _encode_json_type
from datetime import datetime

def _encode_overrides(kvs, overrides, encode_json=False):
    override_kvs = {}
    for k, v in kvs.items():
        if k in overrides:
            exclude = overrides[k].exclude
            # If the exclude predicate returns true, the key should be
            #  excluded from encoding, so skip the rest of the loop
            if exclude and exclude(v):
                continue
            letter_case = overrides[k].letter_case
            original_key = k
            k = letter_case(k) if letter_case is not None else k

            encoder = overrides[original_key].encoder
            v = encoder(v) if encoder is not None else v

        if encode_json:
            v = _encode_json_type(v)
        override_kvs[k] = v
    return override_kvs

# Define a simple class to mimic the Override object
class Override:
    def __init__(self, exclude=None, letter_case=None, encoder=None):
        self.exclude = exclude
        self.letter_case = letter_case
        self.encoder = encoder

def test__encode_overrides_basic():
    kvs = {"name": "Alice", "age": 30}
    overrides = {
        "name": Override(letter_case=str.upper),
        "age": Override(exclude=lambda x: x < 18)
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'NAME': 'Alice', 'age': 30}

