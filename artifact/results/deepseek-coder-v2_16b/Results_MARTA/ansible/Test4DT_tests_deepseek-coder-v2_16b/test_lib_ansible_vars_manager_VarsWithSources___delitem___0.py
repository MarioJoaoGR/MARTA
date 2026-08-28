
import pytest
from ansible.vars.manager import VarsWithSources

def test_edge_case_none():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    with pytest.raises(KeyError):
        del vs['non_existent_key']
