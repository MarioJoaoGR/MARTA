# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with dictionary arguments
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding new variables with sources
def test_add_new_vars():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    vars_with_sources['var3'] = 'source3'
    assert len(vars_with_sources) == 3
    assert vars_with_sources['var3'] == 'source3'

# Test copying the instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert copied_vars['var2'] == 'source2'

# Test accessing variables with sources
def test_access_vars():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test accessing a variable that does not exist (should raise KeyError)
def test_access_nonexistent_var():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    with pytest.raises(KeyError):
        print(vars_with_sources['var3'])  # This should raise a KeyError
