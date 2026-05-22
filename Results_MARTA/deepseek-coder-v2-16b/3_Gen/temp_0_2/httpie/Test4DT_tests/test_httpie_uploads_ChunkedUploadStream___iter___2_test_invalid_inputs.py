
import pytest
from unittest.mock import patch, Mock
from httpie.uploads import ChunkedUploadStream

def test_invalid_inputs():
    with patch('httpie.uploads.ChunkedUploadStream.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            stream = 'not iterable'
            callback = Mock()
            uploader = ChunkedUploadStream(stream, callback)
