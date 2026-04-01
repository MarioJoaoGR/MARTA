
import pytest
from flutes.iterator import drop
from typing import Iterable, Iterator, Type

def test_error_case():
    with pytest.raises(ValueError) as exc_info:
        list(drop(-5, range(10)))
    assert str(exc_info.value) == "`n` should be non-negative"
