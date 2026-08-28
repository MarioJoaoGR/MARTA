
import pytest
from ansible.utils._collections_config import _AnsibleCollectionConfig

# Test for valid inputs
def test_valid_inputs():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    assert config._default_collection is None
    assert config._on_collection_load == _EventSource()
    assert config._collection_finder is None

# Test for edge cases
def test_edge_cases():
    with pytest.raises(TypeError):
        config = _AnsibleCollectionConfig(None, 'my_collection')

# Test for invalid inputs
def test_invalid_inputs():
    meta = {'name': '', 'version': None}
    with pytest.raises(ValueError):
        config = _AnsibleCollectionConfig(meta, 'my_collection')
