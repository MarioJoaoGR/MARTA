
import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, Type

def test_error_case_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))
