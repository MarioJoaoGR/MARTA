
import pytest
from pytutils.sets import MetaSet
import random

class MyMetaFunc:
    def __call__(self, value, **kwargs):
        return 0 if value == 'initial' else 1

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet(meta_func=MyMetaFunc())

def test_invalid_input(meta_set):
    with pytest.raises(TypeError):
        meta_set.add(None)  # Adding None should raise a TypeError
