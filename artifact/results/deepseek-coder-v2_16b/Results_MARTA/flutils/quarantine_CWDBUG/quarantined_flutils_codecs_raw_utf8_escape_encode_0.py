
import pytest
from flutils.codecs.raw_utf8_escape import encode
from typing import Tuple, cast
from functools import reduce

def _each_utf8_hex(text: str) -> list[str]:
    return [f'\\x{ord(c):02x}' for c in text]

@pytest.mark.parametrize("text, expected", [
    ("Hello, World!", b"Hello, World!"),
    ("中文文本", b"\xe4\xb8\xad\xe6\x96\x87\xe6\x9c\xac\xe6\x96\x87"),
    ("Hello, World!", errors='ignore', expected=b"Hello, World!"),
])
def test_encode(text: str, expected: bytes):
    result = encode(text)
    assert isinstance(result[0], bytes)
    assert result[0] == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='? (line 13, col 23)
    ("Hello, World!", errors='ignore', expected=b"Hello, World!"),
"""