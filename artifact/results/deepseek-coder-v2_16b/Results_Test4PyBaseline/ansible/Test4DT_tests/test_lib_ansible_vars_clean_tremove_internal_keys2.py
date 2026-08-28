
import pytest
from ansible.vars.clean import remove_internal_keys

# Example dictionary with internal keys
example_data = {
    'key1': 'value1',
    '_ansible_key2': 'value2',
    'ansible_facts': {
        'discovered_interpreter_python': 'python3',
        'ansible_discovered_interpreter_ruby': 'ruby'
    }
}

def test_remove_internal_keys_empty_dict():
    # Test removing internal keys from an empty dictionary
    data = {}
    remove_internal_keys(data)
    
    assert len(data) == 0, "Expected length of data to be 0 after removing keys"

def test_remove_internal_keys_no_internal_keys():
    # Test the function with a dictionary that has no internal keys
    clean_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    remove_internal_keys(clean_data)
    
    assert len(clean_data) == 2, "Expected length of clean_data to be unchanged after removing keys"

def test_remove_internal_keys_with_exceptions():
    # Test the function with a dictionary that includes an exception key
    data = {
        'key1': 'value1',
        '_ansible_key2': 'value2',
        'ansible_facts': {
            'discovered_interpreter_python': 'python3',
            'ansible_discovered_interpreter_ruby': 'ruby'
        },
        '_ansible_parsed': 'should not be removed'
    }
    remove_internal_keys(data)
    