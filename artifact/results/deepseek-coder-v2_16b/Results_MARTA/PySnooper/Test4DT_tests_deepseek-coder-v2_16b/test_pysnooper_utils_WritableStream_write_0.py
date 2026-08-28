
import pytest
from pysnooper.utils import WritableStream

# Test valid input scenario

# Test edge case with None scenario

# Test invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        writable_stream = WritableStream()