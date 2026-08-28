
# Module: ansible.vars.manager
import pytest
from ansible.vars.manager import VarsWithSources

# Test initialization with a dictionary
def test_init_with_dict():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    assert vars_with_sources['var1'] == 1