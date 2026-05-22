
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedStream

def test_error_handling():
    with patch('httpie.uploads.ChunkedStream.__iter__', side_effect=NotImplementedError):
        mock_chunked_stream = ChunkedStream()
        with pytest.raises(NotImplementedError):
            for _ in mock_chunked_stream:
                pass
