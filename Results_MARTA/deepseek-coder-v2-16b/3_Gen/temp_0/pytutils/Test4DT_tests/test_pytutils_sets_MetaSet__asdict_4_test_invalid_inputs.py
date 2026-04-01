
import pytest
from pytutils.sets import MetaSet
import attr
import random
import copy

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_invalid_inputs(meta_set):
    with pytest.raises(TypeError):
        # Attempt to add a non-hashable type, which should raise a TypeError
        meta_set.add([1, 2, 3])
