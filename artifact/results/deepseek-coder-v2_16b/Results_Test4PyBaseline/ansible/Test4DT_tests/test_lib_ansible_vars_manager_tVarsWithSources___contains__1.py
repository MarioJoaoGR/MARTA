
# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with an empty dictionary
def test_init_with_empty_dict():
    vars_with_sources = VarsWithSources({})
    assert 'var1' not in vars_with_sources

# Test adding a new variable and checking its existence
def test_add_and_contains():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    vars_with_sources['var3'] = 'source3'
    assert 'var3' in vars_with_sources
    assert 'var4' not in vars_with_sources

# Test checking if a variable exists after removing it
def test_remove_variable():
    vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    del vars_with_sources['var1']
    assert 'var1' not in vars_with_sources

# Test checking the existence of a key that is exactly the same as an existing one but with different casing
def test_case_insensitive_contains():
    vars_with_sources = VarsWithSources({'VAR1': 'source1'})
    assert 'var1' not in vars_with_sources  # Case-sensitive check
