
import pytest
from flutes.log import MultiprocessingFileHandler

def test_invalid_input():
    with pytest.raises(TypeError):
        log_handler = MultiprocessingFileHandler(0)  # Passing an integer instead of a string to simulate TypeError
