
import pytest
from flutes.iterator import chunk
from typing import List, Iterable, Iterator



def test_negative_chunks():
    with pytest.raises(ValueError) as e:
        list(chunk(-1, [1, 2, 3]))
    assert str(e.value) == "`n` should be positive"

def test_single_element_chunk():
    result = list(chunk(1, [1, 2, 3]))
    assert result == [[1], [2], [3]]

def test_exact_multiple_chunks():
    result = list(chunk(3, [1, 2, 3, 4, 5]))
    assert result == [[1, 2, 3], [4, 5]]

def test_leftover_elements():
    result = list(chunk(2, [1, 2, 3, 4, 5, 6]))
    assert result == [[1, 2], [3, 4], [5, 6]]