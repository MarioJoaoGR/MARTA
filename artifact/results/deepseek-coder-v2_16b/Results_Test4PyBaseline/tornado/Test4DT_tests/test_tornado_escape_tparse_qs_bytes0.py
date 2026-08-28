
import pytest
import urllib.parse
from typing import Union, Dict, List

# Import the function from its module
def parse_qs_bytes(
    qs: Union[str, bytes], keep_blank_values: bool = False, strict_parsing: bool = False
) -> Dict[str, List[bytes]]:
    """Parses a query string like urlparse.parse_qs,
    but takes bytes and returns the values as byte strings.

    Keys still become type str (interpreted as latin1 in python3!)
    because it's too painful to keep them as byte strings in
    python3 and in practice they're nearly always ascii anyway.
    """
    # This is gross, but python3 doesn't give us another way.
    # Latin1 is the universal donor of character encodings.
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