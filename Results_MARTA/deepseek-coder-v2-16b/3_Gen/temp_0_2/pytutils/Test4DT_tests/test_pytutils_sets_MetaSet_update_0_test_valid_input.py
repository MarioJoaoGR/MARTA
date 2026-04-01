
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def ms():
    return MetaSet()

def test_valid_input(ms):
    lst = [1, 2, 3]
    ms.update(lst)
    assert len(ms._store) == 3
