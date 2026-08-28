
import pytest
from unittest.mock import patch
import urllib.parse
from typing import Dict, List, Union

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

def test_parse_qs_bytes_with_string_input():
    qs = "a=1&b=2"
    expected = {'a': [b'1'], 'b': [b'2']}
    assert parse_qs_bytes(qs) == expected

def test_parse_qs_bytes_with_byte_string_input():
    qs = b"a=1&b=2"
    expected = {'a': [b'1'], 'b': [b'2']}
    assert parse_qs_bytes(qs) == expected

def test_parse_qs_bytes_with_keep_blank_values():
    qs = "a=1&b="
    expected = {'a': [b'1'], 'b': [b'']}
    assert parse_qs_bytes(qs, keep_blank_values=True) == expected

def test_parse_qs_bytes_with_strict_parsing():
    qs = "a=1&b=2&c"
    with pytest.raises(Exception):
        parse_qs_bytes(qs, strict_parsing=True)
