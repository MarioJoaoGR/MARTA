
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_invalid_inputs(meta_set):
    with pytest.raises(TypeError):  # Assuming the function should raise a TypeError for invalid inputs
        meta_set.update(123)  # Example of an invalid input (int instead of iterable)
