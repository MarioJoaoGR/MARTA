
import pytest
import urllib.parse
from typing import Dict, List, Union

def parse_qs_bytes(
    qs: Union[str, bytes], keep_blank_values: bool = False, strict_parsing: bool = False
) -> Dict[str, List[bytes]]:
    """Parses a query string like `urllib.parse.parse_qs`, but takes byte strings and returns the values as byte strings.

    This function converts the input query string (either a byte string or a regular string) to a Unicode string using Latin1 encoding, then parses it with `urllib.parse.parse_qs`. The keys remain in their original form as Unicode strings, which is appropriate for further processing assuming ASCII content. The values are converted back to byte strings using Latin1 encoding before returning.

    Parameters:
        qs (Union[str, bytes]): The query string to be parsed. If provided as a byte string, it will be decoded using Latin1 encoding.
        keep_blank_values (bool): If True, blank values in the query string are kept as empty list. Default is False.
        strict_parsing (bool): If True, raise an exception for any illegal quoting in the query string. Default is False.

    Returns:
        Dict[str, List[bytes]]: A dictionary where keys are Unicode strings and values are lists of byte strings parsed from the query string.
    """
    if isinstance(qs, bytes):
        qs = qs.decode("latin1")
    result = urllib.parse.parse_qs(
        qs, keep_blank_values, strict_parsing, encoding="latin1", errors="strict"
    )
    encoded = {}
    for k, v in result.items():
        encoded[k] = [i.encode("latin1") for i in v]
    return encoded

def test_parse_qs_bytes_basic():
    # Basic usage with string query string
    result = parse_qs_bytes("a=1&b=2")
    assert result == {'a': [b'1'], 'b': [b'2']}

    # Usage with byte string query string
    result = parse_qs_bytes(b"a=1&b=2")
    assert result == {'a': [b'1'], 'b': [b'2']}

    # Usage with keep_blank_values set to True
    result = parse_qs_bytes("a=1&b=", keep_blank_values=True)
    assert result == {'a': [b'1'], 'b': [b'']}
