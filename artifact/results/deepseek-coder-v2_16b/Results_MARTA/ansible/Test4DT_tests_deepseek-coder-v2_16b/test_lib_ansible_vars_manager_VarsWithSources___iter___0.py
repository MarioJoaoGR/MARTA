
import pytest
from ansible.vars.manager import VarsWithSources

# Test scenarios
def test_valid_input():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1
    assert vars_with_sources['var2'] == 2

def test_edge_case():
    vars_with_sources = VarsWithSources()
    with pytest.raises(KeyError):
        vars_with_sources['non_existent_var']

def test_invalid_input():
    vars_with_sources = VarsWithSources({'var1': 1})
    with pytest.raises(KeyError):
        vars_with_sources['var2']
