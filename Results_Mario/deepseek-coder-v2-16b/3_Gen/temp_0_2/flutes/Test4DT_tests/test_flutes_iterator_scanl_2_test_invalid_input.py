
import pytest
from flutes.iterator import scanl
import operator

def test_invalid_input():
    with pytest.raises(ValueError):
        list(scanl(operator.add, [1, 2, 3, 4], 0, "extra"))
