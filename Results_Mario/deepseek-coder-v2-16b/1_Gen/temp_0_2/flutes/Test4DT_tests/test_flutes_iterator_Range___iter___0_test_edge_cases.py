
import pytest
from flutes.iterator import Range

def test_edge_cases():
    # Test with no arguments
    with pytest.raises(ValueError) as excinfo:
        r1 = Range()
    assert str(excinfo.value) == "Range should be called the same way as the builtin `range`"

    # Test with one argument
    r2 = Range(10)
    assert list(r2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test with two arguments
    r3 = Range(1, 10)
    assert list(r3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test with three arguments
    r4 = Range(1, 10, 2)
    assert list(r4) == [1, 3, 5, 7, 9]
