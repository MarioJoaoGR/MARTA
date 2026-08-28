
import pytest
from ansible.vars.manager import VarsWithSources

# Test Scenario 1: Test standard input for __contains__ method
def test_valid_input():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
    assert 'var2' in vars_with_sources
    assert 'var3' not in vars_with_sources

# Test Scenario 2: Test edge cases such as None and empty dictionary
def test_edge_case():
    vars_with_sources = VarsWithSources()
    assert not vars_with_sources
    with pytest.raises(KeyError):
        vars_with_sources['non_existent_key']

# Test Scenario 3: Test invalid inputs to check error handling
def test_invalid_input():
    with pytest.raises(TypeError):
        VarsWithSources(123)  # Passing an integer instead of a dictionary
