
# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding a new variable
def test_add_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1'})
    vars_with_sources['var2'] = 'source2'
    assert len(vars_with_sources) == 2
    assert vars_with_sources['var2'] == 'source2'

# Test accessing a variable
def test_access_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var2'] == 'source2'

# Test deleting a variable
def test_delete_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    del vars_with_sources['var1']
    with pytest.raises(KeyError):
        print(vars_with_sources['var1'])  # This should raise an error

# Test iterating over variables
def test_iterate_over_variables():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert 'var1' in keys and 'var2' in keys

# Test checking if a variable exists
def test_check_variable_existence():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
    assert 'var3' not in vars_with_sources

# Test deleting a variable that does not exist (should raise KeyError)
def test_delete_nonexistent_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    with pytest.raises(KeyError):
        del vars_with_sources['var3']  # This should raise a KeyError
