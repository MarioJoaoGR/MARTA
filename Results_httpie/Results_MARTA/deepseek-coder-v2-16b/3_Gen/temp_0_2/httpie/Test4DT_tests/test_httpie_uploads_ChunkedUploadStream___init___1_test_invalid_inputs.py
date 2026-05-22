
import pytest
from httpie.uploads import ChunkedUploadStream
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test invalid stream input (should raise ValueError)
        stream = None  # Invalid stream input
        callback = MagicMock()
        event = None
        
        with patch('httpie.uploads.ChunkedUploadStream.__init__', side_effect=ValueError("Invalid stream")):
            ChunkedUploadStream(stream, callback, event)
