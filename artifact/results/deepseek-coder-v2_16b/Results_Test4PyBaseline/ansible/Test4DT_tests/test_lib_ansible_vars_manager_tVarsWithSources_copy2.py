
# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding variables and sources
def test_add_vars_and_sources():
    vars_with_sources = VarsWithSources({})
    vars_with_sources['var1'] = 'source1'
    vars_with_sources['var2'] = 'source2'
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test copying the instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert copied_vars['var2'] == 'source2'
    # Ensure that the original and copied instances are different objects
    assert id(vars_with_sources) != id(copied_vars)
    # Ensure that modifications to the copy do not affect the original
    copied_vars['var1'] = 'new_source1'
    assert vars_with_sources['var1'] == 'source1'
    assert copied_vars['var1'] == 'new_source1'

# Test checking the number of variables and existence
def test_methods_and_attributes():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert len(vars_with_sources) == 2
    assert 'var1' in vars_with_sources
    # Ensure that the length of copied instance is also correct
    copied_vars = vars_with_sources.copy()
    assert len(copied_vars) == 2
    assert 'var1' in copied_vars

# Test accessing a non-existent variable
def test_access_nonexistent_var():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    with pytest.raises(KeyError):
        print(vars_with_sources['var3'])  # This should raise a KeyError

# Test copying an empty instance
def test_copy_empty():
    vars_with_sources = VarsWithSources({})
    copied_vars = vars_with_sources.copy()
    assert len(copied_vars) == 0
    # Ensure that the original and copied instances are different objects
    assert id(vars_with_sources) != id(copied_vars)
