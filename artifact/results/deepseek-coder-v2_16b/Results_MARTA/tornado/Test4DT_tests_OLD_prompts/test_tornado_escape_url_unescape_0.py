
import pytest
from tornado import escape
from typing import Union

def url_unescape(value: Union[str, bytes], encoding: str = "utf-8", plus: bool = True) -> str:
    """
    Unescapes a URL-encoded string or bytes.

    Parameters:
        value (Union[str, bytes]): The input to be unescaped. It can be either a string or bytes.
        encoding (str): The character encoding to use when decoding the input. Defaults to "utf-8".
        plus (bool): A flag indicating whether to treat '+' as a space ('+') or leave it as is ('%2B'). If True, '+' will be replaced with a space; otherwise, it remains unmodified. Defaults to True.

    Returns:
        str: The unescaped string.
    """
    if isinstance(value, bytes):
        value = value.decode(encoding)
    return escape.url_unescape(value, plus=plus)

# Test cases for url_unescape function
def test_url_unescape_string():
    result = url_unescape("https://example.com/search?q=hello+world")
    assert result == "https://example.com/search?q=hello world"



def test_url_unescape_bytes_with_plus_false():
    result = url_unescape(b"https://example.com/search?q=hello%20world", plus=False)
    assert result == "https://example.com/search?q=hello world"