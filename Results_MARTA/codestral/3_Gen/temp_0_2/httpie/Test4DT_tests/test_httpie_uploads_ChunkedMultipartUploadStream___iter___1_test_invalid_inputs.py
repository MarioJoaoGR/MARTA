
import pytest
from requests_toolbelt import MultipartEncoder
import threading
from httpie.uploads import ChunkedMultipartUploadStream
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with patch('httpie.uploads.ChunkedMultipartUploadStream.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            encoder = 'invalid'
            event = 'invalid'
            upload_stream = ChunkedMultipartUploadStream(encoder, event)
