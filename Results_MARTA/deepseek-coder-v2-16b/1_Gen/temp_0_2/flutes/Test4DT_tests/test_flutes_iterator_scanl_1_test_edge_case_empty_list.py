
import pytest
from flutes.iterator import scanl

def test_edge_case_empty_list():
    func = lambda x, y: x + y  # Example binary function (addition)
    iterable = []
    
    with pytest.raises(RuntimeError):
        result = list(scanl(func, iterable))
