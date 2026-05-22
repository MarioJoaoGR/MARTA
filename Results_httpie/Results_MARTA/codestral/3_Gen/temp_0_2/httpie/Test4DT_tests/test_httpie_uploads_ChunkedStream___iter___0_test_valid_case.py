
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedStream

def test_valid_case():
    with patch('httpie.uploads.ChunkedStream.__iter__', return_value=iter([b'chunk1', b'chunk2'])):
        chunked_stream = ChunkedStream()
        iterator = iter(chunked_stream)
        assert next(iterator) == b'chunk1'
        assert next(iterator) == b'chunk2'
