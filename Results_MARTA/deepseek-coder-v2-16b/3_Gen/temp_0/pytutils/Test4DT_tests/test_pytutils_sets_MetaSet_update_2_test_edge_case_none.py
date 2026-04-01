
import pytest
from pytutils.sets import MetaSet, consume
import random
import attr

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_edge_case_none(meta_set):
    with pytest.raises(TypeError):
        meta_set.update(None)
