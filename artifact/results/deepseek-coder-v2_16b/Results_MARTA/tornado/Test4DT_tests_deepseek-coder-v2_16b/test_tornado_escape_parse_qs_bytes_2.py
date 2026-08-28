
import pytest
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

# Test cases
def test_valid_input_string():
    qs = 'a=1&b=2'
    expected = {'a': [b'1'], 'b': [b'2']}
    result = parse_qs_bytes(qs)
    assert result == expected

def test_valid_input_bytes():
    qs = b'a=1&b=2'
    expected = {'a': [b'1'], 'b': [b'2']}
    result = parse_qs_bytes(qs)
    assert result == expected

def test_invalid_input_strict_parsing():
    qs = 'a=1&b=2&c'
    with pytest.raises(Exception):
        parse_qs_bytes(qs, strict_parsing=True)
