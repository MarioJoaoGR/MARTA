
import pytest
from ansible.vars.manager import VarsWithSources

def test_valid_key():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'

def test_invalid_input():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    with pytest.raises(KeyError):
        vars_with_sources['non_existent_key']  # This should raise a KeyError as the key does not exist
