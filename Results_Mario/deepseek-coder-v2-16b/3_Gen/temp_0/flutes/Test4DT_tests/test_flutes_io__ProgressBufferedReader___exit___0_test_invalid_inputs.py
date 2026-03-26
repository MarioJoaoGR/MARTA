
import io
from unittest.mock import MagicMock
import pytest
from flutes.io import _ProgressBufferedReader

# Mocking the progress bar function
def test_invalid_inputs():
    raw = io.BytesIO(b'some data')  # Example raw IO base
    bar_fn = MagicMock()  # Assuming this function is defined elsewhere

    with pytest.raises(TypeError):  # Since buffer_size should be an integer and not None
        reader = _ProgressBufferedReader(raw, buffer_size=None, bar_fn=bar_fn)
