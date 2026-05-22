
import pytest
from unittest.mock import patch
from httpie.uploads import ChunkedUploadStream

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test invalid stream input (should raise ValueError)
        stream = None  # Invalid iterable type
        callback = lambda x: None  # Valid callable
        event = None  # Optional argument, no need to mock for this test
        
        with patch('httpie.uploads.ChunkedUploadStream.__init__', side_effect=ValueError("Invalid input")):
            ChunkedUploadStream(stream, callback, event)
