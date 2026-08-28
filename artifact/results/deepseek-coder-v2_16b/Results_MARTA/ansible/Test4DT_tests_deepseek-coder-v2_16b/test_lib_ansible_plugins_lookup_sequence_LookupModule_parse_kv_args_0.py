
import pytest
from ansible.plugins.lookup import sequence

@pytest.fixture(scope="module")
def lookup_module():
    return sequence.LookupModule()

# Test valid inputs
def test_valid_inputs(lookup_module):
    lookup_module.args = {'start': 1, 'end': 5, 'stride': 1, 'format': '%d'}
    result = lookup_module._run([''])
    assert result == ['1', '2', '3', '4', '5']

# Test edge cases with None or empty inputs
def test_edge_cases(lookup_module):
    lookup_module.args = {'start': None, 'end': None, 'stride': None, 'format': None}
    result = lookup_module._run([''])
    assert result == []

# Test invalid inputs that should raise ValueError or TypeError
def test_invalid_inputs(lookup_module):
    with pytest.raises(ValueError):
        lookup_module.args = {'start': 'not an int', 'end': 'also not an int', 'stride': 'neither is this', 'format': 'nor is this'}
        lookup_module._run([''])
