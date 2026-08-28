# Module: ansible.plugins.filter.urls
import pytest
from ansible.plugins.filter.urls import do_urlencode
from six import string_types
from six.moves.urllib.parse import quote  # Importing from urllib to mimic the behavior of url encoding

# Helper function to encode a single value for comparison with the expected output
def helper_do_urlencode(value):
    if isinstance(value, dict):
        return '&'.join([f"{quote(str(k))}={quote(str(v))}" for k, v in value.items()])
    elif not isinstance(value, string_types):
        try:
            iterable = iter(value)
        except TypeError:
            return quote(str(value))
        else:
            encoded_parts = [f"{quote(str(k))}={quote(str(v))}" for k, v in iterable]
            return '&'.join(encoded_parts)
    else:
        return quote(str(value))

# Test cases for do_urlencode function
def test_do_urlencode_string():
    assert do_urlencode("Hello, World!") == helper_do_urlencode("Hello, World!")

def test_do_urlencode_dict():
    assert do_urlencode({"key": "value"}) == helper_do_urlencode({"key": "value"})

def test_do_urlencode_iterable():
    assert do_urlencode([("key", "value")]) == helper_do_urlencode([("key", "value")])

def test_do_urlencode_unsupported_type():
    with pytest.raises(TypeError):
        do_urlencode(12345)

# Additional edge cases can be added to cover more scenarios and ensure robustness of the function.
