
import pytest
from flutes.iterator import Range

def test_edge_case_none():
    with pytest.raises(ValueError) as excinfo:
        r = Range()
    assert str(excinfo.value) == "Range should be called the same way as the builtin `range`"
