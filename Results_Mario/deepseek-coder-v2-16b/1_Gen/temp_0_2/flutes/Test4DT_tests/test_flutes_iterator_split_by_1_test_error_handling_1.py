
import pytest
from flutes.iterator import split_by
from typing import Iterable, List, Callable

def test_error_handling_1():
    with pytest.raises(TypeError):
        iterable = 123
        criterion = lambda x: True
        list(split_by(iterable, empty_segments=False, criterion=criterion))
