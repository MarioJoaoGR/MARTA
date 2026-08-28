
import pytest
from ansible.utils._collections_config import _AnsibleCollectionConfig

# Scenario 1: Test setting a valid collection finder function
def test_valid_input_collection_finder():
    meta = {}
    config = _AnsibleCollectionConfig(meta, 'test_collection')
    
    # Set the collection finder to a lambda function (valid input)
    config.collection_finder(lambda x: x)
    
    # Assert that the collection finder is set correctly
    assert config._collection_finder == lambda x: x

# Scenario 2: Test raising ValueError when trying to set an already configured collection finder
def test_invalid_input_collection_finder():
    meta = {}
    config = _AnsibleCollectionConfig(meta, 'test_collection')
    
    # Set the collection finder to a lambda function (first configuration)
    config.collection_finder(lambda x: x)
    
    # Try to set the collection finder again, which should raise ValueError
    with pytest.raises(ValueError):
        config.collection_finder(lambda y: y)

# Scenario 3: Test missing lines in the function implementation
def test_missing_lines_to_cover():
    meta = {}
    config = _AnsibleCollectionConfig(meta, 'test_collection')
    
    # Check that the collection finder is initially None
    assert config._collection_finder is None
    
    # Check that the default collection and event source are initialized correctly
    assert config._default_collection is None
    assert isinstance(config._on_collection_load, _EventSource)
