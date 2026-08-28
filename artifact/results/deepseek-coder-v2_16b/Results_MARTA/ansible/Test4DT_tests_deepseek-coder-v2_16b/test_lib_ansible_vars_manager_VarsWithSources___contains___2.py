
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
    with pytest.raises(TypeError):
        VarsWithSources(None)
    
    vs = VarsWithSources({})
    assert not any(vs)

# Test Scenario 3: Test invalid inputs that should raise errors
def test_invalid_input():
    with pytest.raises(TypeError):
        vars_with_sources = VarsWithSources(None)
