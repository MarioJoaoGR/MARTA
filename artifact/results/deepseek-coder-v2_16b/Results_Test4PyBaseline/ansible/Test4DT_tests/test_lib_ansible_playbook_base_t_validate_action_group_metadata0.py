# Module: ansible.playbook.base
import pytest
from ansible.playbook.base import _validate_action_group_metadata

# Test cases for _validate_action_group_metadata function

def test_valid_metadata():
    action = {'metadata': {'extend_group': ['item1', 'item2']}}
    found_group_metadata = True
    fq_group_name = 'example_group'
    
    _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
    # No assertions needed as the function should not raise any warnings or errors for valid metadata

def test_missing_metadata():
    action = {'no_metadata': {}}
    found_group_metadata = True
    fq_group_name = 'example_group'
    
    with pytest.warns(UserWarning) as record:
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
        
    assert len(record) == 1
    assert str(record[0].message) == "Invalid metadata was found for action_group example_group while loading module_defaults. The only expected key is metadata, but got keys: no_metadata"

def test_invalid_metadata_type():
    action = {'metadata': {'extend_group': 123}}  # Invalid type (int instead of list)
    found_group_metadata = True
    fq_group_name = 'example_group'
    
    with pytest.warns(UserWarning) as record:
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
        
    assert len(record) == 1
    assert str(record[0].message) == "Invalid metadata was found for action_group example_group while loading module_defaults. The metadata is not a dictionary. Got 123"

def test_unexpected_metadata_keys():
    action = {'metadata': {'extend_group': ['item1', 'item2'], 'extra_key': 'value'}}  # Contains unexpected key
    found_group_metadata = True
    fq_group_name = 'example_group'
    
    with pytest.warns(UserWarning) as record:
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
        
    assert len(record) == 1
    assert str(record[0].message) == "Invalid metadata was found for action_group example_group while loading module_defaults. The metadata contains unexpected keys: extra_key"

def test_unexpected_metadata_types():
    action = {'metadata': {'extend_group': 'not a list'}}  # Invalid type (string instead of list)
    found_group_metadata = True
    fq_group_name = 'example_group'
    
    with pytest.warns(UserWarning) as record:
        _validate_action_group_metadata(action, found_group_metadata, fq_group_name)
        
    assert len(record) == 1
    assert str(record[0].message) == "Invalid metadata was found for action_group example_group while loading module_defaults. The metadata contains unexpected key types: extend_group is not a list (expected type <class 'list'>)"
