# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding a new variable
def test_add_new_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    vars_with_sources['var3'] = 'source3'
    assert vars_with_sources['var3'] == 'source3'

# Test checking if a variable exists
def test_contains():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
    assert 'var3' not in vars_with_sources

# Test copying the instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert copied_vars['var2'] == 'source2'

# Test accessing a variable's source
def test_access_source():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test using the __contains__ method
def test_contains_method():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
    assert 'var3' not in vars_with_sources

# Test iterating over variables
def test_iteration():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert 'var1' in keys and 'var2' in keys

# Test getting the length of variables stored
def test_length():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert len(vars_with_sources) == 2
