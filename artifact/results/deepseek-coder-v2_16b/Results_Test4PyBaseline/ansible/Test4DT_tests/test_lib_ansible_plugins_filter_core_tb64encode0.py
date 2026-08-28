# Module: ansible.plugins.filter.core
import base64
from ansible.plugins.filter.core import b64encode

def test_b64encode_default_encoding():
    encoded_string = b64encode("Hello, World!")
    assert encoded_string == 'SGVsbG8sIFdvcmxkIQ=='

def test_b64encode_invalid_encoding():
    try:
        encoded_string = b64encode("Hello, World!", encoding='ascii')
    except UnicodeEncodeError as e:
        assert str(e) == "'ascii' codec can't encode characters in position 7-11: ordinal not in range(128)"

def test_b64encode_explicit_utf_8():
    encoded_string = b64encode("Hello, World!", encoding='utf-8')
    assert encoded_string == 'SGVsbG8sIFdvcmxkIQ=='
