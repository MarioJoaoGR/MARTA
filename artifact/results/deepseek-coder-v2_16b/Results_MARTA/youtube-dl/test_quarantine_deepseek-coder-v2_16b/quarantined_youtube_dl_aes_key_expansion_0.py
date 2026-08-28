
import pytest
from youtube_dl.aes import key_expansion

def test_error_handling_invalid_length():
    with pytest.raises(ValueError):
        key_expansion([0] * 15)

def test_key_expansion_with_128bit_key():
    assert key_expansion([0] * 16) == [expanded key for 128-bit key]

def test_key_expansion_with_192bit_key():
    assert key_expansion([0] * 24) == [expanded key for 192-bit key]

def test_key_expansion_with_256bit_key():
    assert key_expansion([0] * 32) == [expanded key for 256-bit key]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax. Perhaps you forgot a comma? (line 10, col 40)
    assert key_expansion([0] * 16) == [expanded key for 128-bit key]
"""