
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt import MultipartEncoder
import threading

def test_error_case():
    with patch('httpie.uploads.ChunkedMultipartUploadStream.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            ChunkedMultipartUploadStream('invalid_encoder', 'invalid_event')
