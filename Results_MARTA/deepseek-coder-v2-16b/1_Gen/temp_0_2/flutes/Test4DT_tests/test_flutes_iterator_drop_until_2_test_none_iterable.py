
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator

def test_none_iterable():
    pred_fn = lambda x: x > 5
    iterable = None
    
    with pytest.raises(TypeError):
        list(drop_until(pred_fn, iterable))
