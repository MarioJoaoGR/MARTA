
# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1
    assert vars_with_sources['var2'] == 2

# Test adding variables and sources
def test_add_vars_and_sources():
    vars_with_sources = VarsWithSources({})
    vars_with_sources['var1'] = 'source1'
    vars_with_sources['var2'] = 'source2'
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test copying the instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 1
    assert copied_vars['var2'] == 2
    # Ensure the original and copied instances are distinct
    assert id(vars_with_sources) != id(copied_vars)
    assert vars_with_sources.data is not copied_vars.data
    assert vars_with_sources.sources is not copied_vars.sources

# Test checking the number of variables and existence
def test_methods_and_attributes():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert len(vars_with_sources) == 2
    assert 'var1' in vars_with_sources
    # Ensure non-existing keys are not present
    with pytest.raises(KeyError):
        vars_with_sources['non_existent_key']

# Test adding a new variable and ensuring it exists
def test_add_new_variable():
    vars_with_sources = VarsWithSources({})
    vars_with_sources['new_var'] = 'new_source'
    assert vars_with_sources['new_var'] == 'new_source'
    # Ensure the variable is added correctly
    assert len(vars_with_sources) == 1
    assert 'new_var' in vars_with_sources

# Test deleting a variable and ensuring it does not exist after deletion
def test_delete_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    del vars_with_sources['var1']
    with pytest.raises(KeyError):
        vars_with_sources['var1']
    # Ensure the other variable still exists
    assert vars_with_sources['var2'] == 'source2'
    assert len(vars_with_sources) == 1

# Test iteration over variables
def test_iteration():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert keys == ['var1', 'var2']
