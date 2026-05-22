
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedUploadStream

def test_invalid_inputs():
    with pytest.raises(TypeError):
        stream = 'not iterable'
        callback = MagicMock()
        uploader = ChunkedUploadStream(stream, callback)
        
        for _ in range(3):
            next(uploader.stream)
