# Module: ansible.vars.manager
import pytest
from lib.ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary of variables
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test initialization with no arguments
def test_init_no_args():
    vars_with_sources = VarsWithSources()
    assert len(vars_with_sources.data) == 0
    assert len(vars_with_sources.sources) == 0

# Test adding variables with their sources
def test_add_variables():
    vars_with_sources = VarsWithSources()
    vars_with_sources['var3'] = 'source3'
    vars_with_sources['var4'] = 'source4'
    assert vars_with_sources['var3'] == 'source3'
    assert vars_with_sources['var4'] == 'source4'

# Test copying the instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert len(copied_vars) == len(vars_with_sources)

# Test using __getitem__ and __setitem__
def test_getitem_and_setitem():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    vars_with_sources['var3'] = 'source3'
    assert len(vars_with_sources) == 3

# Test iterating over variables
def test_iteration():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert 'var1' in keys and 'var2' in keys

# Test checking if a key is present
def test_contains():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
