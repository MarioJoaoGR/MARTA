
import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

# Test valid input scenario
def test_valid_input():
    meta = {'name': 'my_collection', 'version': '1.0.0'}
    config = _AnsibleCollectionConfig(meta, 'my_collection')
    
    assert hasattr(config, '_collection_finder'), "Expected _collection_finder to be set"
    assert config._collection_finder is None, "_collection_finder should be initialized to None"
    assert hasattr(config, '_default_collection'), "Expected _default_collection to be set"
    assert config._default_collection is None, "_default_collection should be initialized to None"
    assert isinstance(config._on_collection_load, _EventSource), "_on_collection_load should be an instance of _EventSource"

# Test edge case scenario with None input
def test_edge_case():
    meta = None
    with pytest.raises(TypeError):
        config = _AnsibleCollectionConfig(meta, 'my_collection')

# Test invalid input scenario
def test_invalid_input():
    meta = {'name': '', 'version': ''}  # Invalid metadata
    with pytest.raises(ValueError):
        config = _AnsibleCollectionConfig(meta, 'my_collection')
