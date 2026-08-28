
import pytest
import urllib.parse
from typing import Union, Optional

# Import the function from its module
def url_unescape(  # noqa: F811
    value: Union[str, bytes], encoding: Optional[str] = "utf-8", plus: bool = True
) -> Union[str, bytes]:
    """Decodes the given value from a URL.

    The argument may be either a byte or unicode string.

    If encoding is None, the result will be a byte string.  Otherwise,
    the result is a unicode string in the specified encoding.

    If ``plus`` is true (the default), plus signs will be interpreted
    as spaces (literal plus signs must be represented as "%2B").  This
    is appropriate for query strings and form-encoded values but not
    for the path component of a URL.  Note that this default is the
    reverse of Python's urllib module.

    .. versionadded:: 3.1
       The ``plus`` argument
    """
    if encoding is None:
        if plus:
            # unquote_to_bytes doesn't have a _plus variant, so we use str for decoding to bytes
            value = str(value).replace("+", " ")
        return urllib.parse.unquote_to_bytes(str(value))
    else:
        unquote = urllib.parse.unquote_plus if plus else urllib.parse.unquote
        return unquote(str(value), encoding=encoding)

# Test cases for url_unescape function

def test_default_call():
    assert url_unescape("https%3A//example.com/search?q=hello+world") == "https://example.com/search?q=hello world"

def test_specifying_encoding_as_none():
    result = url_unescape(b"https%3A//example.com/search?q=hello+world", encoding=None)
    assert isinstance(result, bytes), f"Expected bytes but got {type(result)}"

def test_plus_is_true_and_encoding_is_none():
    result = url_unescape("https%3A//example.com/search?q=hello+world", encoding=None)
    assert isinstance(result, bytes), f"Expected bytes but got {type(result)}"

def test_plus_is_false_and_encoding_is_none():
    result = url_unescape("https%3A//example.com/search?q=hello+world", encoding=None, plus=False)