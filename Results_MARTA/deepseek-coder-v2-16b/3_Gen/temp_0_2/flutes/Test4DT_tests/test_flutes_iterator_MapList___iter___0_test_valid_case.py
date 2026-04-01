
from flutes.iterator import MapList
import pytest
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_valid_case():
    a = [1, 2, 3, 4, 5]
    b = MapList(lambda x: x * x, a)
    transformed_elements = list(b)
    
    expected_transformed_elements = [x * x for x in a]
    assert transformed_elements == expected_transformed_elements
