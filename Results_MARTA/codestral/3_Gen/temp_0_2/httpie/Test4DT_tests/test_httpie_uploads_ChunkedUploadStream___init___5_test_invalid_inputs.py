
import pytest
from httpie.uploads import ChunkedUploadStream
from threading import Event
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with patch('httpie.uploads.ChunkedUploadStream.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            uploader = ChunkedUploadStream(None, lambda x: print(x))
