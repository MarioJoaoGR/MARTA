
import pytest
from ansible.config.manager import process

def test_valid_case():
    sample_entry = {'some_key': 'value', 'deprecated': {'message': 'This is deprecated'}}
    expected_output = {'some_key': 'value', 'deprecated': {'message': 'This is deprecated', 'collection_name': 'ansible.builtin'}}
    
    process(sample_entry)
    assert sample_entry == expected_output

def test_missing_case():
    sample_entry = {'some_key': 'value'}
    expected_output = {'some_key': 'value', 'deprecated': {'collection_name': 'ansible.builtin'}}
    
    process(sample_entry)
    assert sample_entry == expected_output

def test_error_case():
    invalid_input = None
    with pytest.raises(KeyError):
        process(invalid_input)
