
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def setup():
    ms = MetaSet()
    return ms

def test_edge_case_empty_list(setup):
    ms = setup
    lst = []
    ms.update(lst)
    assert len(ms._store) == 0, "Expected the store to be empty after updating with an empty list"
