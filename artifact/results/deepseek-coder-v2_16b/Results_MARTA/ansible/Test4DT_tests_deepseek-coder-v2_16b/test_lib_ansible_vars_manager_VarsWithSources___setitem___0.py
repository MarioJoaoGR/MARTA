
import pytest
from ansible.vars.manager import VarsWithSources

# Test valid input scenario
def test_valid_input():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1
    assert vars_with_sources.sources['var1'] is None

# Test handling of None input scenario
def test_none_input():
    vars_with_sources = VarsWithSources(None)
    with pytest.raises(KeyError):
        vars_with_sources['var1']

# Test behavior with invalid key access scenario
def test_invalid_key():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        vars_with_sources['var3']
