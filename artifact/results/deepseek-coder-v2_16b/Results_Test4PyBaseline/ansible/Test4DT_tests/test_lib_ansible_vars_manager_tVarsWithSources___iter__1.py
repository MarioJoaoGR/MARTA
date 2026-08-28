
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1

# Test the __iter__ method returns an iterator over self.data
def test_vars_with_sources_iteration():
    data = {'var1': 1, 'var2': 2}
    vars_with_sources = VarsWithSources(data)
    assert list(vars_with_sources.items()) == list(data.items())
