
import pytest
from pytutils.sets import MetaSet

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_edge_cases(meta_set):
    assert len(meta_set) == 0, "Initial length of the set should be zero"
