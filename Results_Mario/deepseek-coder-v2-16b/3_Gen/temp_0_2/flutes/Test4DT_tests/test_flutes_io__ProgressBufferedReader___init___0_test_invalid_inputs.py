
import pytest
from unittest.mock import MagicMock
from flutes.io import _ProgressBufferedReader

def test_invalid_inputs():
    raw = MagicMock()
    buffer_size = 'invalid'
    bar_fn = lambda x: None
    
    with pytest.raises(TypeError):
        reader = _ProgressBufferedReader(raw, buffer_size=buffer_size, bar_fn=bar_fn)
