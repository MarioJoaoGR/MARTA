
import operator
from pytutils.iters import accumulate
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        list(accumulate(None))
