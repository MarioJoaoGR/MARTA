
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_invalid_input_none():
    with pytest.raises(TypeError):
        list(scanl(lambda x, y: x + y, None))
