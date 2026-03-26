
from flutes.iterator import drop_until
import pytest
from typing import Callable, Iterable, Iterator, Any

def test_invalid_input():
    with pytest.raises(TypeError):
        list(drop_until(lambda x: x > 5, "not an iterable"))
