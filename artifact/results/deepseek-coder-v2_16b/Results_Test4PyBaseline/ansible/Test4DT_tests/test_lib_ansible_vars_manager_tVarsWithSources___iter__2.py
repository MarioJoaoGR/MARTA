
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with an empty dictionary
def test_init_with_empty_dict():
    vars_with_sources = VarsWithSources({})
    assert list(vars_with_sources) == []

# Test initialization with a non-empty dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})