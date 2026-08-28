# Module: tornado.escape
import pytest
from typing import Optional, Union
from tornado.escape import utf8

# Test cases for utf8 function

def test_utf8_none():
    assert utf8(None) is None

def test_utf8_str():
    assert utf8("Hello") == b"Hello"

def test_utf8_bytes():
    assert utf8(b"Hello") == b"Hello"

def test_utf8_unsupported_type():
    with pytest.raises(TypeError):
        utf8(123)
