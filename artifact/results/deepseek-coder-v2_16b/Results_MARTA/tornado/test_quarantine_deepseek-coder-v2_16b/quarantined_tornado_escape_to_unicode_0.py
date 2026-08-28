
import pytest
from typing import Optional, Union

def to_unicode(value: Union[None, str, bytes]) -> Optional[str]:
    """Converts a string argument to a Unicode string.

    This function takes an input which can be `None`, a Unicode string, or a byte string. If the input is already a Unicode string or None, it returns it unchanged. Otherwise, if the input is a byte string, it decodes it using UTF-8 encoding and returns the decoded Unicode string.

    Parameters:
        value (Union[None, str, bytes]): The input string which can be `None`, a Unicode string, or a byte string.

    Returns:
        Optional[str]: A Unicode string if the input was a byte string; otherwise, it returns the unchanged input as a Unicode string or None.

    Raises:
        TypeError: If the input is not one of the expected types (`None`, `str`, `bytes`).

    Examples:
        >>> to_unicode("Hello")
        'Hello'
        
        >>> to_unicode(b"Hello")
        'Hello'
        
        >>> to_unicode(None)
        None
        
        >>> to_unicode(12345)
        Traceback (most recent call last):
            ...
        TypeError: Expected bytes, unicode, or None; got <class 'int'>
    """
```

Here are the test cases for the `to_unicode` function:

```python
import pytest
from typing import Optional, Union

def to_unicode(value: Union[None, str, bytes]) -> Optional[str]:
    if isinstance(value, bytes):
        return value.decode('utf-8')
    elif isinstance(value, str):
        return value
    elif value is None:
        return None
    else:
        raise TypeError("Expected bytes, unicode, or None; got {}".format(type(value).__name__))

# Test cases for to_unicode function

def test_to_unicode_with_unicode_string():
    assert to_unicode("Hello") == "Hello"

def test_to_unicode_with_byte_string():
    assert to_unicode(b"Hello") == "Hello"

def test_to_unicode_with_none():
    assert to_unicode(None) is None

def test_to_unicode_with_invalid_type():
    with pytest.raises(TypeError):
        to_unicode(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 34, col 1)
```
"""