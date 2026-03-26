
import pytest
from flutes.iterator import drop_until

def test_edge_case_none():
    pred_fn = lambda x: x > 5
    iterable = None
    
    with pytest.raises(TypeError):
        list(drop_until(pred_fn, iterable))
