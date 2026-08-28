
import pytest
from dataclasses_json.core import _encode_overrides

# Test cases for _encode_overrides function

def test_basic_usage_with_overrides():
    kvs = {'key': 'value'}
    overrides = {
        'key': type('override', (object,), {
            'exclude': lambda x: False,
            'letter_case': lambda k: k.upper(),
            'encoder': None
        })
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY': 'value'}

def test_excluding_key_based_on_exclude_predicate():
    kvs = {'key': 'value'}
    overrides = {
        'key': type('exclude', (object,), {
            'exclude': lambda x: True,
            'letter_case': None,
            'encoder': None
        })
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {}

def test_using_encode_json_to_apply_json_encoding():
    kvs = {'key': 'value'}
    overrides = {}
    result = _encode_overrides(kvs, overrides, encode_json=True)