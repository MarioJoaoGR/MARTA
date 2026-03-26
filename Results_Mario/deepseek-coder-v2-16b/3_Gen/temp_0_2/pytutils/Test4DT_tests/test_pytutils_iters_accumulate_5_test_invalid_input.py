
import pytest
from pytutils.iters import accumulate
import operator

def test_invalid_input():
    with pytest.raises(TypeError):
        list(accumulate("string"))  # Test invalid input type, such as a string
        list(accumulate([1, 2, "3", 4]))  # Test invalid input within the iterable
        list(accumulate(None))  # Test None input
