
import pytest
from ansible.vars.manager import VarsWithSources

# Test Scenario 1: Test standard input with valid dictionary
def test_valid_input():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    assert vs['var1'] == 1
    assert vs['var2'] == 2

# Test Scenario 2: Test handling of None as an input
def test_none_input():
    vs = VarsWithSources(data=None)
    with pytest.raises(KeyError):
        vs['non_existent_key']

# Test Scenario 3: Test behavior with invalid key access
def test_invalid_key():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        vs['invalid_key']
