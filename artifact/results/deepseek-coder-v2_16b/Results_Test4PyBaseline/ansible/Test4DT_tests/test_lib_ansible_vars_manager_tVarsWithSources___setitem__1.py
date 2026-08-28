
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary containing initial variables and their sources
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert vars_with_sources['var1'] == 'source1'
    assert vars_with_sources['var2'] == 'source2'

# Test adding variables with sources
def test_add_variables():
    vars_with_sources = VarsWithSources()
    vars_with_sources['var3'] = 'source3'
    assert vars_with_sources['var3'] == 'source3'

# Test copying the instance
def test_copy_instance():
    original = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_instance = original.copy()
    assert copied_instance['var1'] == 'source1'
    assert copied_instance['var2'] == 'source2'

# Test iterating over keys in vars_with_sources
def test_iterate_over_keys():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    keys = [key for key in vars_with_sources]
    assert 'var1' in keys and 'var2' in keys

# Test setting and getting variables
def test_set_and_get_variables():
    vars_with_sources = VarsWithSources()
    vars_with_sources['var4'] = 'source4'
    assert vars_with_sources['var4'] == 'source4'

# Test checking for the existence of a variable
def test_check_for_variables():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})