
import pytest
from ansible.vars.manager import VarsWithSources

def test_edge_cases():
    vars_with_sources = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        assert vars_with_sources['non_existent_key'] is None
