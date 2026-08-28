
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
    assert vars_with_sources.get_source('var1') == 'source1'
    assert vars_with_sources.get_source('var2') == 'source2'
    assert vars_with_sources.get_source('var3') is None  # Corrected assertion to match the expected behavior

# Test checking if a key is in the dictionary
def test_contains():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert 'var1' in vars_with_sources
    assert 'var3' not in vars_with_sources

# Test copying the class instance
def test_copy():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    copied_vars = vars_with_sources.copy()
    assert copied_vars['var1'] == 'source1'
    assert copied_vars['var2'] == 'source2'

# Test methods and attributes
def test_methods_and_attributes():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    assert len(vars_with_sources) == 2
    assert vars_with_sources['var1'] == 'source1'
    vars_with_sources['var3'] = 'source3'
    assert len(vars_with_sources) == 3
