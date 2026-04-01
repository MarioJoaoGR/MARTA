
import pytest
from pytutils.iters import accumulate
import operator

def test_invalid_input_none():
    with pytest.raises(TypeError):
        list(accumulate(None))
