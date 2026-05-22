
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import EncodedStream

def test_invalid_input():
    with pytest.raises(TypeError):
        encoded_stream = EncodedStream(mime_overwrite=123, encoding_overwrite='invalid_encoding')
