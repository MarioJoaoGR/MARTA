
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_edge_cases(meta_set):
    assert len(meta_set) == 0
