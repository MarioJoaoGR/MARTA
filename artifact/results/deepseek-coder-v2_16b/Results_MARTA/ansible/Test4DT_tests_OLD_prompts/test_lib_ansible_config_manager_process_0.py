
import pytest
from unittest.mock import patch

def process(entry):
    if 'deprecated' in entry:
        entry['deprecated']['collection_name'] = 'ansible.builtin'

# Test cases
@pytest.fixture
def sample_entry():
    return {'some_key': 'value', 'deprecated': {'message': 'This is deprecated'}}

def test_valid_input(sample_entry):
    process(sample_entry)
    assert 'collection_name' in sample_entry['deprecated']
    assert sample_entry['deprecated']['collection_name'] == 'ansible.builtin'

def test_no_deprecated_section():
    entry = {'some_key': 'value'}
    process(entry)
    assert 'collection_name' not in entry['deprecated'] if 'deprecated' in entry else True

def test_empty_deprecated_section():
    entry = {'some_key': 'value', 'deprecated': {}}
    process(entry)
    assert 'collection_name' in entry['deprecated']
    assert entry['deprecated']['collection_name'] == 'ansible.builtin'
