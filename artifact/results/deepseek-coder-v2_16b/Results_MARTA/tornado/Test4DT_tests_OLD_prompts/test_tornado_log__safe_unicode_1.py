
import pytest
from unittest.mock import patch
from tornado.log import _safe_unicode, _unicode

def test_safe_unicode_with_bytes():
    with patch('tornado.log._unicode', return_value='mocked_unicode'):
        result = _safe_unicode(b"Hello, World!")
        assert result == 'mocked_unicode'

