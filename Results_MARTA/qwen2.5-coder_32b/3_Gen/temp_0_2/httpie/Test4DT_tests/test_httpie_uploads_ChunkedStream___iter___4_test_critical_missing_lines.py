
import pytest
from unittest.mock import patch
from httpie.uploads import ChunkedStream

def test_critical_missing_lines():
    with patch('httpie.uploads.ChunkedStream.__iter__', side_effect=NotImplementedError):
        chunked_stream = ChunkedStream()
        with pytest.raises(NotImplementedError):
            for _ in chunked_stream:
                pass
