
import pytest
from pysnooper.utils import WritableStream

# Test for valid input scenario
def test_valid_input():
    with pytest.raises(TypeError):
        writable_stream = WritableStream()
