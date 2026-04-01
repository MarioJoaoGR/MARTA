
import pytest
from flutes.iterator import split_by
from typing import Iterable, List, Iterator

def test_error_case():
    with pytest.raises(ValueError):
        list(split_by([1, 2, 3]))
