
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, Type

def test_invalid_input():
    with pytest.raises(TypeError):
        list(drop_until(lambda x: x > 5, None))
