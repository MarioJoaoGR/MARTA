
import pytest
from ansible.vars.clean import remove_internal_keys

# Example dictionary with internal keys and non-internal keys
example_data = {
    'key1': 'value1',
    '_ansible_key2': 'value2',
    'ansible_facts': {
        'discovered_interpreter_python': 'python3',
        'ansible_discovered_interpreter_ruby': 'ruby'
    },
    'warnings': [],
    'deprecations': []
}

def test_remove_internal_keys_empty_lists():
    # Test removing empty lists for warnings and deprecations
    data = {
        'warnings': [],
        'deprecations': []
    }
    remove_internal_keys(data)
    
    assert 'warnings' not in data, "Expected 'warnings' to be removed"
    assert 'deprecations' not in data, "Expected 'deprecations' to be removed"

def test_remove_internal_keys_no_modification():
    # Test the function with a dictionary that has no internal keys
    clean_data = {
        'key1': 'value1',
        'ansible_facts': {}
    }
    remove_internal_keys(clean_data)
    
    assert len(clean_data) == 2, "Expected length of clean_data to be 2 after removing keys"

def test_remove_internal_keys_with_non_internal_keys():
    # Test the function with a dictionary that has non-internal keys
    data = {
        'key1': 'value1',
        '_ansible_key2': 'value2',
        'ansible_facts': {
            'discovered_interpreter_python': 'python3',
            'ansible_discovered_interpreter_ruby': 'ruby'
        },
        'warnings': [],
        'deprecations': []
    }
    remove_internal_keys(data)
    
    assert '_ansible_key2' not in data, "Expected '_ansible_key2' to be removed"
    assert 'ansible_facts' in data, "Expected 'ansible_facts' to remain"
    assert 'discovered_interpreter_python' not in data['ansible_facts'], "Expected 'discovered_interpreter_python' to be removed from 'ansible_facts'"
    assert 'ansible_discovered_interpreter_ruby' not in data['ansible_facts'], "Expected 'ansible_discovered_interpreter_ruby' to be removed from 'ansible_facts'"