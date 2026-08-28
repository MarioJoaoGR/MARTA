
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with an initial variable set
def test_init_with_initial_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1'})
    assert vars_with_sources['var1'] == 'source1'

# Test adding multiple variables at once during initialization
def test_init_with_multiple_variables():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding a variable using __setitem__ method
def test_add_variable():
    vars_with_sources = VarsWithSources()
    vars_with_sources['var3'] = 'source3'