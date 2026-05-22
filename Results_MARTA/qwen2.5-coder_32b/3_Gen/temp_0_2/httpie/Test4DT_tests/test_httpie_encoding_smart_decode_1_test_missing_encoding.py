
import pytest
from unittest.mock import patch, MagicMock
from httpie.encoding import smart_decode, detect_encoding

def test_missing_encoding():
    content = b'Hello, World!'
    with patch('httpie.encoding.detect_encoding', return_value='utf-8'):
        decoded_content, detected_encoding = smart_decode(content, '')
        assert isinstance(decoded_content, str)
        assert detected_encoding == 'utf-8'
