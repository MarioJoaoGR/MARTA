
from io import StringIO
import pytest
from isort.core import process
from isort.settings import DEFAULT_CONFIG, Config

def test_process_with_none_output_stream():
    # Test with None as output stream
    input_stream = StringIO("some code")
    with pytest.raises(AttributeError):
        process(input_stream, None)
