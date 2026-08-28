
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding a new variable with source
def test_add_new_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    vars_with_sources['var3'] = 'source3'
    assert vars_with_sources['var3'] == 'source3'

# Test accessing a variable's source
def test_get_source():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})