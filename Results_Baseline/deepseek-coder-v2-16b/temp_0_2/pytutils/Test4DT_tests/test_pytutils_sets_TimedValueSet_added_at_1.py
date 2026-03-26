
import pytest
from pytutils.sets import MetaSet  # Replace with the actual module name if different

@pytest.fixture
def meta_set():
    return MetaSet()

# Test case to check the existence of _meta attribute and its type
def test_meta_attribute(meta_set):
    assert hasattr(meta_set, '_meta'), "MetaSet instance should have a _meta attribute"
    assert isinstance(meta_set._meta, dict), "_meta attribute should be an instance of dictionary"
