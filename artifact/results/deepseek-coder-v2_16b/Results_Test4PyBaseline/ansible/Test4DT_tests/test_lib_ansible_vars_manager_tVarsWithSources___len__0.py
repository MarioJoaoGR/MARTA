# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with provided arguments and keyword arguments
def test_init():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding a new variable with its source
def test_setitem():
    vars_with_sources = VarsWithSources({'var1': 'source1'})
    vars_with_sources['var2'] = 'source2'
    assert vars_with_sources['var2'] == 'source2'

# Test deleting a variable
def test_delitem():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    del vars_with_sources['var1']
    with pytest.raises(KeyError):
        print(vars_with_sources['var1'])

# Test iteration over keys
def test_iter():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert 'var1' in keys and 'var2' in keys

# Test length method
def test_len():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert len(vars_with_sources) == 2

# Test contains method
def test_contains():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources and 'var3' not in vars_with_sources

# Test copying the class instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert copied_vars['var2'] == 'source2'
