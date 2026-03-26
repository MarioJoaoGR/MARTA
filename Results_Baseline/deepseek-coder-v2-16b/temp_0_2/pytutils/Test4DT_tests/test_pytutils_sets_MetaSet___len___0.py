
import pytest
import random
import attr
from pytutils.sets import MetaSet

# Fixture to create a new instance of MetaSet for each test
@pytest.fixture
def meta_set():
    return MetaSet()

def test_initialization(meta_set):
    assert isinstance(meta_set, MetaSet)
    assert len(meta_set._store) == 0