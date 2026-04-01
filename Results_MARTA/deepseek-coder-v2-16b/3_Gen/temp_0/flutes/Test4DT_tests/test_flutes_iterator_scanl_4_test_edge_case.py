
import pytest
from flutes.iterator import scanl
import operator

def test_empty_list():
    with pytest.raises(RuntimeError):
        result = list(scanl(operator.add, []))
