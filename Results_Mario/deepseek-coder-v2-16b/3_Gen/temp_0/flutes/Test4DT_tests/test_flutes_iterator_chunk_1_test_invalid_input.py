
import pytest
from typing import Iterable, List, Iterator
from flutes.iterator import chunk

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        list(chunk(-1, range(10)))
    assert str(excinfo.value) == "`n` should be positive"
