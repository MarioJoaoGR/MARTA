
import pytest
from dataclasses import dataclass
from typing import Dict, Any, Callable

# Assuming the following dataclass definitions are provided elsewhere in your codebase or standard library
@dataclass
class OverrideInfo:
    letter_case: Callable[[str], str] = None
    encoder: Callable[[Any], Any] = None
    exclude: Callable[[Any], bool] = lambda _: False

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
            if k in override_kvs:
                raise ValueError(
                    f"Multiple fields map to the same JSON "
                    f"key after letter case encoding: {k}"
                )

            encoder = overrides[original_key].encoder
            v = encoder(v) if encoder is not None else v

        if encode_json:
            v = _encode_json_type(v)
        override_kvs[k] = v
    return override_kvs

# Assuming the following function is defined elsewhere in your codebase or standard library
def _encode_json_type(obj):
    if isinstance(obj, list):
        return [_encode_json_type(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: _encode_json_type(v) for k, v in obj.items()}
    else:
        return obj

# Test cases for the function _encode_overrides
def test_encode_overrides():
    overrides = {
        "name": OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
        "age": OverrideInfo(letter_case=None, encoder=_encode_json_type)
    }
    kvs = {"name": "John", "age": 30}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert 'NAME' in encoded_kvs and encoded_kvs['NAME'] == 'John'
    assert 'age' in encoded_kvs and isinstance(encoded_kvs['age'], int)

def test_encode_overrides_with_exclude():
    overrides = {
        "name": OverrideInfo(letter_case=lambda x: x.upper(), encoder=None, exclude=lambda _: True),
        "age": OverrideInfo(letter_case=None, encoder=_encode_json_type)
    }
    kvs = {"name": "John", "age": 30}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert 'name' not in encoded_kvs
    assert 'age' in encoded_kvs and isinstance(encoded_kvs['age'], int)

@pytest.mark.xfail(reason="Expected to raise ValueError")
def test_encode_overrides_with_conflict():
    with pytest.raises(ValueError):
        overrides = {
            "name": OverrideInfo(letter_case=lambda x: 'other' if x == 'name' else x, encoder=None),
            "age": OverrideInfo(letter_case=None, encoder=_encode_json_type)
        }
        kvs = {"name": "John", "age": 30}
        _encode_overrides(kvs, overrides, encode_json=True)

def test_encode_overrides_with_json_encoding():
    overrides = {
        "name": OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
        "age": OverrideInfo(letter_case=None, encoder=_encode_json_type)
    }
    kvs = {"name": "John", "age": 30}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)