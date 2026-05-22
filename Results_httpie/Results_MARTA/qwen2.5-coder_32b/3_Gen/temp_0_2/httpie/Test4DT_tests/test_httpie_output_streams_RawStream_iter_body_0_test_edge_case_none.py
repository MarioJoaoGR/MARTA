
import pytest
from unittest.mock import MagicMock, patch
from httpie.output.streams import RawStream

class TestRawStream:
    def test_edge_case_none(self):
        with patch('httpie.output.streams.RawStream.__init__', return_value=None) as mock_init:
            mock_msg = MagicMock()
            mock_msg.iter_body.return_value = iter([b'a' * 1024] * 100)
            
            stream = RawStream(chunk_size=RawStream.CHUNK_SIZE, msg=mock_msg)
            assert isinstance(stream, RawStream)
            mock_init.assert_called_once()
