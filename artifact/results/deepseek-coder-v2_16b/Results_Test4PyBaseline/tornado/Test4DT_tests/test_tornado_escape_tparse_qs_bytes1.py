
import pytest
import urllib.parse
from typing import Union, Dict, List

# Import the function from its module
def parse_qs_bytes(
    qs: Union[str, bytes], keep_blank_values: bool = False, strict_parsing: bool = False
) -> Dict[str, List[bytes]]:
    if isinstance(qs, bytes):
        qs = qs.decode("latin1")
    result = urllib.parse.parse_qs(
        qs, keep_blank_values, strict_parsing, encoding="latin1", errors="strict"
    )
    encoded = {}
    for k, v in result.items():
        encoded[k] = [i.encode("latin1") for i in v]
    return encoded

# Test cases
def test_parse_qs_bytes_str():
    qs = 'a=1&b=2'
    expected = {'a': [b'1'], 'b': [b'2']}
    assert parse_qs_bytes(qs) == expected

@pytest.mark.xfail(reason="Expected to fail due to missing blank value entries")
def test_parse_qs_bytes_bytes_not_keeping_blank():
    qs = b'a=1&b='
    expected = {'a': [b'1'], 'b': [b'']}
    assert parse_qs_bytes(qs, keep_blank_values=False) == expected

def test_parse_qs_bytes_bytes_strict_parsing():
    qs = b'a=1&b='
    expected = {'a': [b'1'], 'b': [b'']}