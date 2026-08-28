# Module: ansible.vars.clean
import pytest
from ansible.vars.clean import clean_facts

# Test Case 1: Basic Usage
def test_clean_facts_basic():
    original_facts = {
        'ansible_os': 'Linux',
        '_ansible_key1': 'should be removed',
        'nested': {'_ansible_key2': 'also should be removed'}
    }
    cleaned_facts = clean_facts(original_facts)
    assert cleaned_facts == {'ansible_os': 'Linux', 'nested': {}}

# Test Case 2: Handling Nested Dictionaries
def test_clean_facts_nested():
    nested_facts = {
        'ansible_os': 'Linux',
        'nested': {
            '_ansible_key1': 'should be removed',
            '_ansible_key2': 'also should be removed'
        }
    }
    cleaned_nested_facts = clean_facts(nested_facts)
    assert cleaned_nested_facts == {'ansible_os': 'Linux', 'nested': {}}

# Test Case 3: Handling Empty Dictionary
def test_clean_facts_empty():
    empty_facts = {}
    cleaned_empty_facts = clean_facts(empty_facts)
    assert cleaned_empty_facts == {}

# Test Case 4: Handling Dictionary with No Restricted Keys
def test_clean_facts_no_restricted_keys():
    no_restricted_keys = {
        'ansible_os': 'Linux',
        'some_other_key': 'value'
    }
    cleaned_no_restricted_keys = clean_facts(no_restricted_keys)
    assert cleaned_no_restricted_keys == {'ansible_os': 'Linux', 'some_other_key': 'value'}

# Test Case 5: Handling Dictionary with Specific Restricted Keys
def test_clean_facts_specific_restricted_keys():
    specific_restricted_keys = {
        'ansible_os': 'Linux',
        'ansible_ssh_host_key_rsa': 'should not be removed'
    }
    cleaned_specific_restricted_keys = clean_facts(specific_restricted_keys)
    assert cleaned_specific_restricted_keys == {'ansible_os': 'Linux', 'ansible_ssh_host_key_rsa': 'should not be removed'}
