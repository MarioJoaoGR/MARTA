
import pytest
from unittest.mock import patch
from tornado.log import _safe_unicode, _unicode

def test_safe_unicode_with_unicode_string():
    result = _safe_unicode("Hello, World!")
    assert isinstance(result, str)
    assert result == "Hello, World!"

