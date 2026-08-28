
import pytest
from httpie.uploads import ChunkedUploadStream
from io import BytesIO
from unittest.mock import patch, call

def process_chunk(chunk):
    print("Processing chunk:", chunk)

# Test for valid inputs
def test_valid_inputs():
    file_stream = BytesIO(b'a'*1024)
    upload_stream = ChunkedUploadStream(stream=file_stream, callback=process_chunk)
    
    with patch('builtins.print') as mock_print:
        for chunk in upload_stream:
            pass  # Just iterating over the stream to trigger the callback

    assert 'Processing chunk:' in str(mock_print.call_args_list[0][0][0])

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        ChunkedUploadStream()  # Should raise TypeError as it lacks required parameters
