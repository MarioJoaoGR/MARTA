
import pytest
from pytutils.sets import MetaSet

@pytest.fixture(name="meta_set")
def create_meta_set():
    return MetaSet()

def test_invalid_input(meta_set):
    with pytest.raises(TypeError):
        len(None)  # This should raise a TypeError because None is not an instance of MetaSet
