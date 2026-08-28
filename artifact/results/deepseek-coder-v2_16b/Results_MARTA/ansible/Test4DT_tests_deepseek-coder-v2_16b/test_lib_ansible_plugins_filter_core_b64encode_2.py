
import pytest
from ansible.plugins.filter.core import b64encode

def test_b64encode_default_encoding():
    result = b64encode("Hello, World!")
    assert result == 'SGVsbG8sIFdvcmxkIQ=='


def test_b64encode_specific_encoding():
    result = b64encode("Hello, World!", encoding='utf-8')
    assert result == 'SGVsbG8sIFdvcmxkIQ=='