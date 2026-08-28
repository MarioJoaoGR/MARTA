
import pytest
from unittest.mock import patch
from tornado.escape import utf8

def test_edge_cases():
    with pytest.raises(TypeError):
        utf8(12345)

@patch('tornado.escape.utf8', side_effect=utf8)
def test_mocked_tornado_utf8(mock_utf8):
    assert mock_utf8("Hello") == b'Hello'
    assert mock_utf8(b"World") == b'World'
    with pytest.raises(TypeError):
        mock_utf8(12345)
